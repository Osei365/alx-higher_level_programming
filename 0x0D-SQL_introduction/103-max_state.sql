-- get max of temperature by states

SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state ASC
LIMIT 3;
