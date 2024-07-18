DELIMITER $$

DROP PROCEDURE IF EXISTS sp_delete_member $$

CREATE PROCEDURE sp_delete_member(
    IN p_manager_id INT,
    IN p_member_id INT
)
BEGIN
    DECLARE manager_role ENUM('support', 'manager', 'member');
    DECLARE member_role ENUM('support', 'manager', 'member');

    SELECT role INTO manager_role
    FROM Users
    WHERE user_id = p_manager_id;

    SELECT role INTO member_role
    FROM Users
    WHERE user_id = p_member_id;

    IF manager_role = 'manager' THEN
        IF member_role = 'member' THEN
            DELETE FROM Users WHERE user_id = p_member_id;
            SELECT 'Member deleted successfully' AS success_message;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Cannot delete user with role other than member';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only managers can delete members';
    END IF;
END$$

DELIMITER ;
