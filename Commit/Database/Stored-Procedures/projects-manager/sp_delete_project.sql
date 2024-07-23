DELIMITER $$

DROP PROCEDURE IF EXISTS sp_delete_project $$

CREATE PROCEDURE sp_delete_project(
    IN p_project_id INT
)
BEGIN
    DECLARE v_project_exists INT;

    SELECT COUNT(*) INTO v_project_exists
    FROM Projects
    WHERE project_id = p_project_id;

    IF v_project_exists = 0 THEN
        SELECT 'Error: The project does not exist' AS message;
    ELSE
        DELETE FROM Projects
        WHERE project_id = p_project_id;
        
        SELECT 'Success: Project deleted successfully' AS message;
    END IF;
END$$

DELIMITER ;
