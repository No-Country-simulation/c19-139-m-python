DELIMITER $$

DROP PROCEDURE IF EXISTS sp_user_login $$

CREATE PROCEDURE sp_user_login(
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255)
)
BEGIN
    DECLARE v_user_id INT;
    DECLARE v_user_role VARCHAR(255);
    DECLARE v_password_hash VARCHAR(255);
    DECLARE hashedPassword VARCHAR(255);

    SET hashedPassword = SHA2(p_password, 256);

    SELECT user_id, password_hash, role INTO v_user_id, v_password_hash, v_user_role
    FROM Users
    WHERE email = p_email;

    IF v_user_id IS NULL THEN
        SELECT u.user_id, u.password_hash, 'member' AS role INTO v_user_id, v_password_hash, v_user_role
        FROM Users u
        JOIN Project_Members pm ON u.user_id = pm.user_id
        WHERE u.email = p_email;
    END IF;

    IF v_user_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid email or password';
    ELSE
        IF v_password_hash = hashedPassword THEN
            SELECT 
                v_user_id AS user_id,
                v_user_role AS role;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Invalid email or password';
        END IF;
    END IF;
END$$

DELIMITER ;
