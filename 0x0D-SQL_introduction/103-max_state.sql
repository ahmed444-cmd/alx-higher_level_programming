-- Display max tempretature of all states
-- Order by state

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
