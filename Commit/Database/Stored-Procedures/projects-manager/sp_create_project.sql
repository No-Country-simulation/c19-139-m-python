DELIMITER $$

DROP PROCEDURE IF EXISTS sp_create_project $$

CREATE PROCEDURE sp_create_project(
    IN p_manager_id INT,
    IN p_name VARCHAR(255),
    IN p_description TEXT,
    IN p_start_date DATE,
    IN p_due_date DATE
)
BEGIN
    DECLARE v_manager_exists INT;
    DECLARE v_project_exists INT;

    SELECT COUNT(*) INTO v_manager_exists
    FROM Users
    WHERE user_id = p_manager_id AND role = 'manager';

    IF v_manager_exists = 0 THEN
        SELECT 'Error: The manager does not exist or is not a manager' AS message;
    ELSE
        SELECT COUNT(*) INTO v_project_exists
        FROM Projects
        WHERE manager_id = p_manager_id AND name = p_name;

        IF v_project_exists > 0 THEN
            SELECT 'Error: A project with this name already exists for this manager' AS message;
        ELSE
            INSERT INTO Projects (manager_id, name, description, start_date, due_date, status)
            VALUES (p_manager_id, p_name, p_description, p_start_date, p_due_date, 'not started');
            
            SELECT 'Success: Project created successfully' AS message;
        END IF;
    END IF;
END$$

DELIMITER ;
