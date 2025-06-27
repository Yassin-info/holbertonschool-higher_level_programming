-- create database if doesnt exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user02 if doesnt exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- give privilege SELECT to user2 on database2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- apply change
FLUSH PRIVILEGES;
