DELIMITER $$

DROP PROCEDURE IF EXISTS sp_count_completed_tasks $$

CREATE PROCEDURE sp_count_completed_tasks(
    IN p_manager_id INT,
    IN p_project_id INT
)
BEGIN
    DECLARE project_manager INT;

    SELECT manager_id INTO project_manager
    FROM Projects
    WHERE project_id = p_project_id;

    IF p_manager_id = project_manager THEN
        SELECT 
            priority,
            COUNT(*) AS task_count
        FROM Tasks
        WHERE project_id = p_project_id AND status = 'completed'
        GROUP BY priority;

    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only the manager who created the project can view tasks';
    END IF;
END$$

DELIMITER ;
