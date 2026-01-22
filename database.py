import sqlite3
from student import Student

class Database:
    def __init__(self, db_path="students.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                class_name TEXT,
                phone TEXT
            )
        ''')
        self.conn.commit()

    def add_student(self, student: Student):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO students (first_name, last_name, class_name, phone)
            VALUES (?, ?, ?, ?)
        ''', (student.first_name, student.last_name, student.class_name, student.phone))
        self.conn.commit()
        return cursor.lastrowid

    def get_all_students(self):
        cursor = self.conn.execute("SELECT id, first_name, last_name, class_name, phone FROM students")
        rows = cursor.fetchall()
        return [Student(row[0], row[1], row[2], row[3], row[4]) for row in rows]

    def close(self):
        self.conn.close()
