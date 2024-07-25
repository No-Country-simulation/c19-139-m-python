DELIMITER $$

DROP PROCEDURE IF EXISTS sp_list_manager_projects $$

CREATE PROCEDURE sp_list_manager_projects(
    IN p_manager_id INT
)
BEGIN
    DECLARE manager_role ENUM('support', 'manager', 'member');

    SELECT role INTO manager_role
    FROM Users
    WHERE user_id = p_manager_id;

    IF manager_role = 'manager' THEN
        SELECT 
            p.project_id,
            p.name AS project_name,
            p.description,
            p.start_date,
            p.due_date,
            p.status,
            p.created_at
        FROM 
            Projects p
        WHERE 
            p.manager_id = p_manager_id;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only managers can list their projects';
    END IF;
END$$

DELIMITER ;
