DELIMITER $$

DROP PROCEDURE IF EXISTS sp_edit_task $$

CREATE PROCEDURE sp_edit_task(
    IN p_task_id INT,
    IN p_assigned_member_id INT,
    IN p_status ENUM('to do', 'in progress', 'completed')
)
BEGIN
    DECLARE task_owner INT;
    
    SELECT assigned_member_id INTO task_owner
    FROM Tasks
    WHERE task_id = p_task_id;
    
    IF task_owner = p_assigned_member_id THEN
        UPDATE Tasks
        SET status = p_status
        WHERE task_id = p_task_id;

        SELECT 'Task updated successfully' AS success_message;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'You do not have permission to edit this task.';
    END IF;
END $$

DELIMITER ;
