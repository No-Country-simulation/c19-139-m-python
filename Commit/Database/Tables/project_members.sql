DROP TABLE IF EXISTS Project_Members;

CREATE TABLE Project_Members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    project_id INT,
    role VARCHAR(255),
    seniority ENUM('trainee', 'junior', 'senior'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);
