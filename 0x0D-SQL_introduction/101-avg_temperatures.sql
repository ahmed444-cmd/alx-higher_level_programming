-- Displays the average temperature by city
-- Ordered by temperature desc

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
