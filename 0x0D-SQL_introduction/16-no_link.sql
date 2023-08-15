-- list rows from second_table without
-- listing rows that don't have a name

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
