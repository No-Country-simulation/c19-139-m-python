DELIMITER $$

DROP PROCEDURE IF EXISTS sp_view_project_details $$

CREATE PROCEDURE sp_view_project_details(
    IN p_project_id INT,
    IN p_manager_id INT
)
BEGIN
    DECLARE manager_role ENUM('support', 'manager', 'member');
    DECLARE project_count INT;

    SELECT role INTO manager_role
    FROM Users
    WHERE user_id = p_manager_id;

    IF manager_role = 'manager' THEN
        SELECT COUNT(*) INTO project_count
        FROM Projects
        WHERE project_id = p_project_id AND manager_id = p_manager_id;

        IF project_count = 1 THEN
            SELECT 
                p.project_id,
                p.name AS project_name,
                p.description,
                p.start_date,
                p.due_date,
                p.status
            FROM 
                Projects p
            WHERE 
                p.project_id = p_project_id;

            SELECT 
                pm.member_id,
                pm.member_name,
                pm.member_email,
                pm.role,
                pm.seniority,
                pm.availability
            FROM 
                Project_Members pm
            WHERE 
                pm.project_id = p_project_id;

            SELECT 
                t.task_id,
                t.title,
                t.description,
                t.status,
                t.priority,
                t.due_date,
                u.name AS assigned_to_name
            FROM 
                Tasks t
                LEFT JOIN Users u ON t.assigned_member_id = u.user_id
            WHERE 
                t.project_id = p_project_id;

            SELECT 
                IFNULL((SELECT COUNT(*) FROM Tasks WHERE project_id = p_project_id AND status = 'completed'), 0) /
                IFNULL((SELECT COUNT(*) FROM Tasks WHERE project_id = p_project_id), 1) * 100 AS project_progress;

            SELECT 
                t.task_id,
                t.title,
                t.description,
                t.due_date,
                t.status
            FROM 
                Tasks t
            WHERE 
                t.project_id = p_project_id AND t.due_date < CURDATE() AND t.status <> 'completed';

            SELECT 
                IFNULL((SELECT COUNT(*) FROM Tasks WHERE project_id = p_project_id AND status = 'completed' AND due_date >= CURDATE()), 0) /
                IFNULL((SELECT COUNT(*) FROM Tasks WHERE project_id = p_project_id), 1) * 100 AS on_time_completion_rate;

            SELECT 
                t.status,
                COUNT(*) AS task_count
            FROM 
                Tasks t
            WHERE 
                t.project_id = p_project_id
            GROUP BY 
                t.status;

            SELECT 
                t.priority,
                t.status,
                COUNT(*) AS task_count
            FROM 
                Tasks t
            WHERE 
                t.project_id = p_project_id
            GROUP BY 
                t.priority, t.status;

            SELECT 
                u.name AS assigned_to_name,
                t.status,
                COUNT(*) AS task_count
            FROM 
                Tasks t
                LEFT JOIN Users u ON t.assigned_member_id = u.user_id
            WHERE 
                t.project_id = p_project_id
            GROUP BY 
                u.name, t.status;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Manager does not own this project or the project does not exist.';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only managers can view project details.';
    END IF;
END$$

DELIMITER ;
