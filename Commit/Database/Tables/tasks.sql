DROP TABLE IF EXISTS Tasks;

CREATE TABLE Tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT,
    assigned_to INT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('to do', 'in progress', 'completed') DEFAULT 'to do',
    priority ENUM('low', 'medium', 'high') DEFAULT 'medium',
    start_date DATE,
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id),
    FOREIGN KEY (assigned_to) REFERENCES Users(user_id)
);
