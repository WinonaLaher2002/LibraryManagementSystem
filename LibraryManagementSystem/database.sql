CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    borrowed_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    student_fullname VARCHAR(255),
    student_id VARCHAR(50)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

--update the username and password into admin_username and admin_password--
ALTER TABLE admins
CHANGE COLUMN username admin_username VARCHAR(255) NOT NULL,
CHANGE COLUMN password admin_password VARCHAR(255) NOT NULL;

CREATE TABLE admin_register (
    id INT AUTO_INCREMENT PRIMARY KEY,
    admin_username VARCHAR(255) UNIQUE NOT NULL,
    admin_password VARCHAR(255) NOT NULL,
    admin_confirm_password VARCHAR(255) NOT NULL
);

CREATE TABLE register (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    confirm_password VARCHAR(255) NOT NULL
);



