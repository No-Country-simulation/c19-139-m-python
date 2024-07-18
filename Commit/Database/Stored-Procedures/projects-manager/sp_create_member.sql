DELIMITER $$

DROP PROCEDURE IF EXISTS sp_create_member $$

CREATE PROCEDURE sp_create_member(
    IN p_manager_id INT,
    IN p_member_name VARCHAR(255),
    IN p_member_email VARCHAR(255),
    IN p_member_password VARCHAR(60)
)
BEGIN
    DECLARE manager_role ENUM('support', 'manager', 'member');
    DECLARE user_count INT;
    DECLARE hashedPassword VARCHAR(256);

    SET hashedPassword = SHA2(p_member_password, 256);

    SELECT role INTO manager_role
    FROM Users
    WHERE user_id = p_manager_id;

    IF manager_role = 'manager' THEN
        SELECT COUNT(*) INTO user_count
        FROM Users
        WHERE email = p_member_email;

        IF user_count = 0 THEN
            INSERT INTO Users (name, email, password_hash, role)
            VALUES (p_member_name, p_member_email, hashedPassword, 'member');

            SELECT 'Member created successfully' AS success_message;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'A user with this email already exists';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only managers can create new members';
    END IF;
END$$

DELIMITER ;
