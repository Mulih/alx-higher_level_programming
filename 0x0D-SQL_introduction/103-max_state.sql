-- Displays the max temperature of each State

SELECT state, MAX(`value`) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state
