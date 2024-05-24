-- Lists all records in the table except those wil no name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
