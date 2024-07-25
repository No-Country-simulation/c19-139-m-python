DELIMITER $$

DROP PROCEDURE IF EXISTS sp_create_task $$

CREATE PROCEDURE sp_create_task(
    IN p_manager_id INT,
    IN p_project_id INT,
    IN p_title VARCHAR(255),
    IN p_description TEXT,
    IN p_status ENUM('to do', 'in progress', 'completed'),
    IN p_priority ENUM('low', 'medium', 'high'),
    IN p_start_date DATE,
    IN p_due_date DATE
)
BEGIN
    DECLARE project_manager INT;
    DECLARE task_exists INT;

    SELECT manager_id INTO project_manager
    FROM Projects
    WHERE project_id = p_project_id;

    IF p_manager_id = project_manager THEN
        SELECT COUNT(*) INTO task_exists
        FROM Tasks
        WHERE title = p_title AND project_id = p_project_id;

        IF task_exists = 0 THEN
            INSERT INTO Tasks (
                project_id, title, description, status, priority, start_date, due_date
            ) VALUES (
                p_project_id, p_title, p_description, p_status, p_priority, p_start_date, p_due_date
            );

            SELECT 'Task created successfully' AS success_message;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'A task with this title already exists in the specified project.';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only the manager who created the project can create tasks.';
    END IF;
END$$

DELIMITER ;
