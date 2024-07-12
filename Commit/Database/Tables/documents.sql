DROP TABLE IF EXISTS Documents;

CREATE TABLE Documents (
    document_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT,
    uploaded_by INT,
    title VARCHAR(255) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id),
    FOREIGN KEY (uploaded_by) REFERENCES Users(user_id)
);
