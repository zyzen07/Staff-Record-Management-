 
SELECT * FROM complaints;
 
USE complaints_managements1;
SELECT DATABASE();
SHOW TABLES;
CREATE TABLE IF NOT EXISTS complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    live_location VARCHAR(255),
    uploaded_file VARCHAR(255),
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SHOW TABLES;
SELECT * FROM complaints;
ALTER TABLE complaints ADD COLUMN action_taken VARCHAR(225);
SHOW TABLES;





