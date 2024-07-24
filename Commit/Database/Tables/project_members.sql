DROP TABLE IF EXISTS Project_Members;

CREATE TABLE Project_Members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT,
    role VARCHAR(255),
    seniority ENUM('trainee', 'junior', 'senior'),
    availability ENUM('free', 'busy') DEFAULT 'free',
    member_email VARCHAR(255) UNIQUE NOT NULL,
    member_name VARCHAR(255) NOT NULL,
    member_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);
