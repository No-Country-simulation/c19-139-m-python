DELIMITER $$

DROP PROCEDURE IF EXISTS sp_get_free_members $$

CREATE PROCEDURE sp_get_free_members()
BEGIN
    SELECT u.user_id, u.name, u.email, p.seniority
    FROM Users u
    LEFT JOIN Project_Members pm ON u.user_id = pm.user_id
    WHERE u.role = 'member' AND pm.user_id IS NULL;
END$$

DELIMITER ;
