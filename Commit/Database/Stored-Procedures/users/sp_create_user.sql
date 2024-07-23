DELIMITER $$

DROP PROCEDURE IF EXISTS sp_create_user $$
CREATE PROCEDURE sp_create_user(
    IN p_name VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(60)
)
BEGIN
    DECLARE user_count INT;
    DECLARE hashedPassword VARCHAR(256);

    SET hashedPassword = SHA2(p_password, 256);

    SELECT COUNT(*) INTO user_count
    FROM Users
    WHERE email = p_email;

    IF user_count = 0 THEN
        INSERT INTO Users (name, email, password_hash, role)
        VALUES (p_name, p_email, hashedPassword, 'manager');
        SELECT 'User created successfully as manager' AS success_message;
    ELSE
        SIGNAL SQLSTATE '45000'
        SELECT 'A user with this email already exists' AS message;
    END IF;
END$$
DELIMITER ;
