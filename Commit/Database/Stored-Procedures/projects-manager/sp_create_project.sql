DELIMITER $$

DROP PROCEDURE IF EXISTS sp_create_project $$
CREATE PROCEDURE sp_create_project(
    IN p_manager_id INT,
    IN p_project_name VARCHAR(255),
    IN p_description TEXT
)
BEGIN
    DECLARE manager_role ENUM('support', 'manager', 'member');

    SELECT role INTO manager_role
    FROM Users
    WHERE user_id = p_manager_id;

    IF manager_role = 'manager' THEN
        INSERT INTO Projects (name, description, created_by)
        VALUES (p_project_name, p_description, p_manager_id);
        SELECT 'Project created successfully' AS success_message;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only managers can create projects';
    END IF;
END$$
DELIMITER ;
