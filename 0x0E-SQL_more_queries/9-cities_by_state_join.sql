-- Write a script that lists all cities contained in the database
SELECT DISTINCT cities.id, cities.name, states.name FROM cities JOIN states
ON cities.id = states.id;
