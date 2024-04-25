SELECT s.name AS subject_name
FROM subjects s
JOIN grades g ON s.subject_id = g.subject_id
WHERE g.student_id = 1 AND s.teacher_id = 1;