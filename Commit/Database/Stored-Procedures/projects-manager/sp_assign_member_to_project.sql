DELIMITER $$

DROP PROCEDURE IF EXISTS sp_assign_member_to_project $$

CREATE PROCEDURE sp_assign_member_to_project(
    IN p_manager_id INT,
    IN p_project_id INT,
    IN p_member_email VARCHAR(255),
    IN p_role VARCHAR(255),
    IN p_seniority ENUM('trainee', 'junior', 'senior')
)
BEGIN
    DECLARE manager_role ENUM('support', 'manager', 'member');
    DECLARE project_creator INT;
    DECLARE member_id INT;

    SELECT role INTO manager_role
    FROM Users
    WHERE user_id = p_manager_id;

    SELECT manager_id INTO project_creator
    FROM Projects
    WHERE project_id = p_project_id;

    IF manager_role = 'manager' AND project_creator = p_manager_id THEN
        SELECT user_id INTO member_id
        FROM Users
        WHERE email = p_member_email AND role = 'member';

        IF member_id IS NOT NULL THEN
            INSERT INTO Project_Members (user_id, project_id, role, seniority)
            VALUES (member_id, p_project_id, p_role, p_seniority);

            SELECT 'Member assigned to project successfully' AS success_message;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No member found with this email';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only the manager who created the project can assign members';
    END IF;
END$$

DELIMITER ;
