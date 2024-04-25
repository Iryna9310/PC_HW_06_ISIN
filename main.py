import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

# Підключення до бази даних
conn = sqlite3.connect('university.db')
c = conn.cursor()

# Створення таблиць
c.execute('''CREATE TABLE students (
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            group_id INTEGER)''')

c.execute('''CREATE TABLE groups (
            group_id INTEGER PRIMARY KEY,
            name TEXT)''')

c.execute('''CREATE TABLE teachers (
            teacher_id INTEGER PRIMARY KEY,
            name TEXT)''')

c.execute('''CREATE TABLE subjects (
            subject_id INTEGER PRIMARY KEY,
            name TEXT,
            teacher_id INTEGER)''')

c.execute('''CREATE TABLE grades (
            grade_id INTEGER PRIMARY KEY,
            student_id INTEGER,
            subject_id INTEGER,
            grade INTEGER,
            date_received TEXT)''')

# Вставка випадкових даних за допомогою Faker
fake = Faker()

# Додавання груп
groups = ['Group A', 'Group B', 'Group C']
for group_name in groups:
    c.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))
    conn.commit()

# Додавання викладачів
teachers = [fake.name() for _ in range(5)]
for teacher_name in teachers:
    c.execute("INSERT INTO teachers (name) VALUES (?)", (teacher_name,))
    conn.commit()

# Додавання студентів
for _ in range(30):
    student_name = fake.name()
    group_id = random.randint(1, 3)  # Випадкове призначення до групи
    c.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (student_name, group_id))
    conn.commit()

# Додавання предметів
subjects = [('Mathematics', 1), ('Physics', 2), ('Biology', 3), ('Chemistry', 4), ('History', 5)]
for subject in subjects:
    c.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", subject)
    conn.commit()

# Додавання оцінок для студентів
for student_id in range(1, 31):
    for subject_id in range(1, 6):
        grade = random.randint(60, 100)  # Випадкові оцінки
        date_received = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
        c.execute("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)",
                  (student_id, subject_id, grade, date_received))
        conn.commit()

# Закриваємо з'єднання з базою даних
conn.close()