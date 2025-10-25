-- Count the number of records for each score and sort by count in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
