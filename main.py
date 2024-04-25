import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="your_db_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()

fake = Faker()

# Функція для генерації випадкових даних для студентів
def generate_students(num_students):
    groups = [1, 2, 3]  # Припустимо, у нас є 3 групи
    for _ in range(num_students):
        full_name = fake.name()
        group_id = random.choice(groups)
        cur.execute("INSERT INTO Students (full_name, group_id) VALUES (%s, %s)", (full_name, group_id))
    conn.commit()

# Функція для генерації випадкових даних для груп
def generate_groups():
    groups = ["Group A", "Group B", "Group C"]
    for group_name in groups:
        cur.execute("INSERT INTO Groups (group_name) VALUES (%s)", (group_name,))
    conn.commit()

# Функція для генерації випадкових даних для викладачів
def generate_professors(num_professors):
    for _ in range(num_professors):
        full_name = fake.name()
        cur.execute("INSERT INTO Professors (full_name) VALUES (%s)", (full_name,))
    conn.commit()

# Функція для генерації випадкових даних для предметів
def generate_subjects(num_subjects):
    for _ in range(num_subjects):
        subject_name = fake.job()
        professor_id = random.randint(1, 3)  # Припустимо, у нас є 3 викладачі
        cur.execute("INSERT INTO Subjects (subject_name, professor_id) VALUES (%s, %s)", (subject_name, professor_id))
    conn.commit()

# Функція для генерації випадкових даних для оцінок
def generate_grades(num_grades):
    students = [i for i in range(1, 51)]  # Припустимо, у нас є 50 студентів
    subjects = [i for i in range(1, 11)]  # Припустимо, у нас є 10 предметів
    for _ in range(num_grades):
        student_id = random.choice(students)
        subject_id = random.choice(subjects)
        grade = round(random.uniform(2, 5), 2)  # Оцінки від 2 до 5
        date_received = fake.date_between(start_date='-1y', end_date='today')
        cur.execute("INSERT INTO Grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s)",
                    (student_id, subject_id, grade, date_received))
    conn.commit()

# Створення тестових даних
generate_groups()
generate_professors(3)
generate_subjects(10)
generate_students(50)
generate_grades(1000)

# Закриття з'єднання
cur.close()
conn.close()