-- lists the number of records with the same score in the table second_table

SELECT count(score)
FROM second_table
WHERE score = name;
