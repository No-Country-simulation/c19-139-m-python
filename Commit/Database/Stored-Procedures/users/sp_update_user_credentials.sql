DELIMITER $$

DROP PROCEDURE IF EXISTS sp_update_user_credentials $$

CREATE PROCEDURE sp_update_user_credentials(
    IN p_email VARCHAR(255),
    IN p_new_email VARCHAR(255),
    IN p_new_password VARCHAR(60)
)
BEGIN
    DECLARE hashedPassword VARCHAR(256);
    DECLARE v_user_exists INT DEFAULT 0;

    IF p_new_password IS NOT NULL THEN
        SET hashedPassword = SHA2(p_new_password, 256);
    END IF;

    UPDATE Users
    SET 
        email = IFNULL(p_new_email, email),
        password_hash = IFNULL(hashedPassword, password_hash)
    WHERE email = p_email;

    SET v_user_exists = ROW_COUNT();

    IF v_user_exists = 0 THEN
        UPDATE Project_Members
        SET 
            member_email = IFNULL(p_new_email, member_email),
            member_password = IFNULL(hashedPassword, member_password)
        WHERE member_email = p_email;

        SET v_user_exists = ROW_COUNT();
    END IF;

    IF v_user_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'User not found';
    ELSE
        SELECT 'User credentials updated successfully' AS success_message;
    END IF;
END$$

DELIMITER ;
