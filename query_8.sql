SELECT AVG(g.grade) AS average_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.subject_id
WHERE s.teacher_id = 2;