-- creates the table unique_id on your MySQL server
-- creates a table in data base
CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
