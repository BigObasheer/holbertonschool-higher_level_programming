-- Lists all of the cities of California
SELECT `cities`.id, cities.name
       FROM `states`, `cities`
       WHERE cities.state_id = states.id
       AND states.name = 'California';
