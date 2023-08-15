-- select and list scores distinctly

SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
