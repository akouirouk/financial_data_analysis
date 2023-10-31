-- @block create database
CREATE DATABASE IF NOT EXISTS paysim;
-- @block select database
USE paysim;
-- @block create table
CREATE TABLE IF NOT EXISTS transactions (
    id INT NOT NULL AUTO_INCREMENT,
    hour INT NOT NULL,
    type VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    initiator_id VARCHAR(11) NOT NULL,
    initiator_old_balance DECIMAL(10, 2) NOT NULL,
    initiator_new_balance DECIMAL(10, 2) NOT NULL,
    target_id VARCHAR(11) NOT NULL,
    target_old_balance DECIMAL(10, 2) NOT NULL,
    target_new_balance DECIMAL(10, 2) NOT NULL,
    is_fraud INT(1) NOT NULL,
    PRIMARY KEY (id)
);
-- @block load CSV file from local machine to table
LOAD DATA INFILE './data/output/cleaned_paysim_data.csv' IGNORE INTO TABLE transactions FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';