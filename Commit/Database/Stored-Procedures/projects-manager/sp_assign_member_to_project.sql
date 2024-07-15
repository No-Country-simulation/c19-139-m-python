DELIMITER $$

DROP PROCEDURE IF EXISTS sp_assign_member_to_project $$
CREATE PROCEDURE sp_assign_member_to_project(
    IN p_manager_id INT,
    IN p_project_id INT,
    IN p_member_name VARCHAR(255),
    IN p_member_email VARCHAR(255),
    IN p_member_password VARCHAR(60)
)
BEGIN
    DECLARE manager_role ENUM('support', 'manager', 'member');
    DECLARE project_creator INT;
    DECLARE user_count INT;
    DECLARE hashedPassword VARCHAR(256);
    DECLARE member_id INT;

    SET hashedPassword = SHA2(p_member_password, 256);

    SELECT role INTO manager_role
    FROM Users
    WHERE user_id = p_manager_id;

    SELECT manager_id INTO project_creator
    FROM Projects
    WHERE project_id = p_project_id;

    IF manager_role = 'manager' AND project_creator = p_manager_id THEN

        SELECT COUNT(*) INTO user_count
        FROM Users
        WHERE email = p_member_email;

        IF user_count = 0 THEN
            INSERT INTO Users (name, email, password_hash, role)
            VALUES (p_member_name, p_member_email, hashedPassword, 'member');
            
            SELECT LAST_INSERT_ID() INTO member_id;

            INSERT INTO Project_Members (user_id, project_id, role)
            VALUES (member_id, p_project_id, 'member');

            SELECT 'Member created and assigned to project successfully' AS success_message;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'A user with this email already exists';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only the manager who created the project can assign members';
    END IF;
END$$
DELIMITER ;
