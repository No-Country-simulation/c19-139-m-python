DROP TABLE IF EXISTS Reports;

CREATE TABLE Reports (
    report_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT,
    generated_by INT,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id),
    FOREIGN KEY (generated_by) REFERENCES Users(user_id)
);
