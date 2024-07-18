DELIMITER $$

DROP PROCEDURE IF EXISTS sp_assign_task $$
CREATE PROCEDURE sp_assign_task(
    IN p_task_id INT,
    IN p_assigned_to INT
)
BEGIN
    DECLARE assigned_member_seniority ENUM('trainee', 'junior', 'senior');
    DECLARE task_priority ENUM('low', 'medium', 'high');
    DECLARE error_message VARCHAR(255);

    SELECT priority INTO task_priority
    FROM Tasks
    WHERE task_id = p_task_id;

    SELECT seniority INTO assigned_member_seniority
    FROM Project_Members
    WHERE user_id = p_assigned_to;

    IF assigned_member_seniority = 'trainee' AND task_priority != 'low' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Trainees can only be assigned to tasks with low priority';
    
    ELSEIF assigned_member_seniority = 'senior' AND task_priority = 'low' THEN
        UPDATE Tasks
        SET assigned_to = p_assigned_to
        WHERE task_id = p_task_id;
        SET error_message = 'Warning: You are assigning a senior to a low priority task.';
    
    ELSE
        UPDATE Tasks
        SET assigned_to = p_assigned_to
        WHERE task_id = p_task_id;
    END IF;

    IF error_message IS NOT NULL THEN
        SELECT error_message AS success_message;
    ELSE
        SELECT 'Task assigned successfully' AS success_message;
    END IF;
END$$

DELIMITER ;
