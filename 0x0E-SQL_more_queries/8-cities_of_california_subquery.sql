-- select cities from states

SELECT id, name FROM cities
WHERE state_id = (
	SELECT id from states
	WHERE name = 'California'
)
ORDER BY id ASC;
