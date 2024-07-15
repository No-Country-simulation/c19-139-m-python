DELIMITER $$

DROP PROCEDURE IF EXISTS sp_user_login $$

CREATE PROCEDURE sp_user_login(
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255)
)
BEGIN
    DECLARE v_user_id INT;
    DECLARE v_user_role ENUM('support', 'manager', 'member');
    DECLARE v_password_hash VARCHAR(255);

    SELECT user_id, password_hash, role INTO v_user_id, v_password_hash, v_user_role
    FROM Users
    WHERE email = p_email;

    IF v_user_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid email or password';
    ELSE
        IF v_password_hash = p_password THEN
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
