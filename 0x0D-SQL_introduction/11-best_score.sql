-- selects two columns that meet a condition
-- condition is score must be >= 0

SELECT score, name FROM second_table
WHERE score >= 10
ORDER by score DESC;
