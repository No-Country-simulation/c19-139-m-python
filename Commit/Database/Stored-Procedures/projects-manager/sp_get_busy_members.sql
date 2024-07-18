DELIMITER $$

DROP PROCEDURE IF EXISTS sp_get_busy_members $$

CREATE PROCEDURE sp_get_busy_members()
BEGIN
    SELECT u.user_id, u.name, u.email, p.name AS project_name, pm.role, pm.seniority
    FROM Users u
    JOIN Project_Members pm ON u.user_id = pm.user_id
    JOIN Projects p ON pm.project_id = p.project_id
    WHERE u.role = 'member';
END$$

DELIMITER ;
