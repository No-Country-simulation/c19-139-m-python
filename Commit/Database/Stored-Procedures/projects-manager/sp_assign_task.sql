DELIMITER $$

DROP PROCEDURE IF EXISTS sp_assign_task $$
CREATE PROCEDURE sp_assign_task(
    IN p_task_id INT,
    IN p_assigned_to INT
)
BEGIN
    DECLARE assigned_member_seniority ENUM('trainee', 'junior', 'senior');
    DECLARE task_priority ENUM('low', 'medium', 'high');

    SELECT priority INTO task_priority
    FROM Tasks
    WHERE task_id = p_task_id;

    SELECT seniority INTO assigned_member_seniority
    FROM Project_Members
    WHERE user_id = p_assigned_to;

    IF (task_priority = 'high' AND assigned_member_seniority = 'senior') OR
       (task_priority = 'medium' AND (assigned_member_seniority = 'senior' OR assigned_member_seniority = 'junior')) OR
       (task_priority = 'low') THEN
        UPDATE Tasks
        SET assigned_to = p_assigned_to
        WHERE task_id = p_task_id;
        SELECT 'Task assigned successfully' AS success_message;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The member does not have the appropriate seniority for this task priority';
    END IF;
END$$
DELIMITER ;
