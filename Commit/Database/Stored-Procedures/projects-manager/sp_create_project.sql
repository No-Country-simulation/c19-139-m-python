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

    SELECT COUNT(*) INTO v_manager_exists
    FROM Users
    WHERE user_id = p_manager_id AND role = 'manager';

    IF v_manager_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The manager does not exist or is not a manager';
    ELSE
        INSERT INTO Projects (manager_id, name, description, start_date, due_date, status)
        VALUES (p_manager_id, p_name, p_description, p_start_date, p_due_date, 'not started');
    END IF;
END$$

DELIMITER ;
