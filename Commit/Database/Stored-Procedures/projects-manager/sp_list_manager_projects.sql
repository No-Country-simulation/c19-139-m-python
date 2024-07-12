DELIMITER $$

DROP PROCEDURE IF EXISTS sp_list_manager_projects $$
CREATE PROCEDURE sp_list_manager_projects(
    IN p_manager_id INT
)
BEGIN
    DECLARE manager_role ENUM('support', 'manager', 'member');

    SELECT role INTO manager_role
    FROM Users
    WHERE user_id = p_manager_id;

    IF manager_role = 'manager' THEN
        SELECT 
            p.project_id,
            p.project_name,
            COUNT(pm.user_id) AS member_count
        FROM 
            Projects p
            LEFT JOIN Project_Members pm ON p.project_id = pm.project_id
        WHERE 
            p.manager_id = p_manager_id
        GROUP BY 
            p.project_id, p.project_name;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Only managers can list their projects';
    END IF;
END$$
DELIMITER ;
