DELIMITER $$

DROP PROCEDURE IF EXISTS sp_create_task $$

CREATE PROCEDURE sp_create_task(
    IN p_manager_id INT,
    IN p_project_id INT,
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_assigned_to INT,
    IN p_status ENUM('to do', 'in progress', 'completed'),
    IN p_priority ENUM('low', 'medium', 'high'),
    IN p_start_date DATE,
    IN p_due_date DATE
)
BEGIN
    DECLARE project_manager INT;

    SELECT manager_id INTO project_manager
    FROM Projects
    WHERE project_id = p_project_id;

    IF p_manager_id = project_manager THEN
        INSERT INTO Tasks (
            project_id, assigned_to, title, description, status, priority, start_date, due_date
        ) VALUES (
            p_project_id, p_assigned_to, p_title, p_description, p_status, p_priority, p_start_date, p_due_date
        );

        SELECT 'Task created successfully' AS success_message;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only the manager who created the project can create tasks';
    END IF;
END$$

DELIMITER ;
