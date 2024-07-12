DROP TABLE IF EXISTS Projects;

CREATE TABLE Projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    manager_id INT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    start_date DATE,
    due_date DATE,
    status ENUM('not started', 'in progress', 'completed') DEFAULT 'not started',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (manager_id) REFERENCES Users(user_id)
);
