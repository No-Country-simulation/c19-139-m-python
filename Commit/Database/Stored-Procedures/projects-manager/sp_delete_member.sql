DELIMITER $$

DROP PROCEDURE IF EXISTS sp_create_member $$

CREATE PROCEDURE sp_create_member(
    IN p_manager_id INT,
    IN p_project_id INT,
    IN p_member_email VARCHAR(255),
    IN p_member_name VARCHAR(255),
    IN p_member_password VARCHAR(255),
    IN p_role VARCHAR(255),
    IN p_seniority ENUM('trainee', 'junior', 'senior')
)
BEGIN
    DECLARE project_exists INT;
    DECLARE member_email_exists INT;

    SELECT COUNT(*) INTO project_exists
    FROM Tasks
    WHERE project_id = p_project_id;

    IF project_exists > 0 THEN
        SELECT COUNT(*) INTO member_email_exists
        FROM Project_Members
        WHERE member_email = p_member_email;

        IF member_email_exists = 0 THEN
            INSERT INTO Project_Members (
                project_id, role, seniority, availability, member_email, member_name, member_password
            )
            VALUES (
                p_project_id, p_role, p_seniority, 'free', p_member_email, p_member_name, SHA2(p_member_password, 256)
            );
            SELECT 'Member created and assigned to project successfully' AS success_message;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'A member with this email already exists.';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot create member. No tasks found for the specified project.';
    END IF;
END$$

DELIMITER ;
