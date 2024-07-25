DELIMITER $$

DROP PROCEDURE IF EXISTS sp_create_member $$

CREATE PROCEDURE sp_create_member(
    IN p_manager_id INT,
    IN p_project_id INT,
    IN p_member_name VARCHAR(255),
    IN p_member_email VARCHAR(255),
    IN p_member_password VARCHAR(60),
    IN p_role VARCHAR(255),
    IN p_seniority ENUM('trainee', 'junior', 'senior'),
    IN p_availability ENUM('free', 'busy')
)
BEGIN
    DECLARE manager_role ENUM('support', 'manager', 'member');
    DECLARE member_exists INT;

    DECLARE hashedPassword VARCHAR(256);
    SET hashedPassword = SHA2(p_member_password, 256);

    SELECT role INTO manager_role
    FROM Users
    WHERE user_id = p_manager_id;

    IF manager_role = 'manager' THEN
        IF (SELECT COUNT(*) FROM Projects WHERE project_id = p_project_id AND manager_id = p_manager_id) = 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'The manager does not have a relationship with the specified project';
        END IF;

        SELECT COUNT(*) INTO member_exists
        FROM Project_Members
        WHERE member_email = p_member_email AND project_id = p_project_id;

        IF member_exists = 0 THEN
            INSERT INTO Project_Members (project_id, member_name, member_email, member_password, role, seniority, availability)
            VALUES (p_project_id, p_member_name, p_member_email, hashedPassword, p_role, p_seniority, p_availability);

            SELECT 'Member created successfully and assigned to project' AS success_message;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'A member with this email already exists in the specified project';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only managers can create new members';
    END IF;
END$$

DELIMITER ;
