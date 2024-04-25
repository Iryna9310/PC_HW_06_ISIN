SELECT gr.name AS group_name, AVG(g.grade) AS average_grade
FROM groups gr
JOIN students s ON gr.group_id = s.group_id
JOIN grades g ON s.student_id = g.student_id
WHERE g.subject_id = 2
GROUP BY gr.group_id;