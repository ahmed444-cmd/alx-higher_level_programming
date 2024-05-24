-- Displays the average temperature of 3 cities
-- During July and August
-- Ordered by temperature desc

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
