-- Displays average temperatures by city in descending order

SELECT `city`, AVG(value) avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY avg_temp DESC;
