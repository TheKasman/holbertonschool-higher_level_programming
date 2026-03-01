-- Say my name
-- You're heisenberg
-- You're god damn right
SELECT score, name
FROM second_table
WHERE
    name IS NOT NULL
    AND name != ''
ORDER BY score DESC