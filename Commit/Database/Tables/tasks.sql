DROP TABLE IF EXISTS Tasks;

CREATE TABLE Tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT,
    assigned_member_id INT,
    title VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    status ENUM('to do', 'in progress', 'completed') DEFAULT 'to do',
    priority ENUM('low', 'medium', 'high') DEFAULT 'medium',
    start_date DATE,
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id),
    FOREIGN KEY (assigned_member_id) REFERENCES Project_Members(member_id)
);
