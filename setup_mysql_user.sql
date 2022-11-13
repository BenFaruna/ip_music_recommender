-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS music_dev_db;
CREATE IF NOT EXISTS USER 'music_dev'@'localhost' IDENTIFIED BY 'music_dev_pwd';
GRANT ALL PRIVILEGES ON `music_dev_db`.* TO 'music_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'music_dev'@'localhost';
FLUSH PRIVILEGES;
