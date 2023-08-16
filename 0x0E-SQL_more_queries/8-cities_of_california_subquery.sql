-- select cities from states

SELECT cities.id, cities.name FROM cities
WHERE states.state_id = (
	SELECT states.id from states
	WHERE states.name = 'California'
)
ORDER BY cities.id ASC;
