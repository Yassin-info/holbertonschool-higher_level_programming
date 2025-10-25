-- List records from second_table, excluding rows without names, sorted by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
