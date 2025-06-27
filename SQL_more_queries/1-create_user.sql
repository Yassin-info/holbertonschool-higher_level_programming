-- create user_0d_1 if doesnt exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- give all grants to user1 on all database and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
