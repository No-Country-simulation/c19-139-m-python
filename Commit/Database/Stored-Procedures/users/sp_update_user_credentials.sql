DELIMITER $$

DROP PROCEDURE IF EXISTS sp_update_user_credentials $$
CREATE PROCEDURE sp_update_user_credentials(
    IN p_user_id INT,
    IN p_new_email VARCHAR(255),
    IN p_new_password VARCHAR(60)
)
BEGIN
    DECLARE hashedPassword VARCHAR(256);

    IF p_new_password IS NOT NULL THEN
        SET hashedPassword = SHA2(p_new_password, 256);
    END IF;

    UPDATE Users
    SET 
        email = IFNULL(p_new_email, email),
        password_hash = IFNULL(hashedPassword, password_hash)
    WHERE user_id = p_user_id;

    SELECT 'User credentials updated successfully' AS success_message;
END$$
DELIMITER ;
