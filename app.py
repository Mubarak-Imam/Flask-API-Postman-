#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "Welcome to the Flask API"

if __name__ == '__main__':
    app.run(debug=True)


# In[2]:


#Implementing the Create Operation


# In[3]:


@app.route('/students', methods=['POST'])
def create_student():
    new_student = request.get_json()
    student_id = new_student['student_id']
    first_name = new_student['first_name']
    last_name = new_student['last_name']
    dob = new_student['dob']
    amount_due = new_student['amount_due']

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO students (student_id, first_name, last_name, dob, amount_due) VALUES (?, ?, ?, ?, ?)",
              (student_id, first_name, last_name, dob, amount_due))
    conn.commit()
    conn.close()
    return jsonify(new_student), 201


# In[4]:


#Implementing the Read Operation


# In[5]:


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE student_id = ?', (student_id,)).fetchone()
    conn.close()

    if student is None:
        return jsonify({'error': 'Student not found'}), 404

    return jsonify(dict(student))


# In[6]:


#Implementing the Update Operation


# In[7]:


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    updated_student = request.get_json()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('UPDATE students SET first_name = ?, last_name = ?, dob = ?, amount_due = ? WHERE student_id = ?',
              (updated_student['first_name'], updated_student['last_name'], updated_student['dob'], updated_student['amount_due'], student_id))
    conn.commit()
    conn.close()
    return jsonify(updated_student)


# In[8]:


#Implementing the Delete Operation


# In[9]:


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
    conn.commit()
    conn.close()
    return '', 204


# In[10]:


#Displaying All Records


# In[11]:


@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return jsonify([dict(student) for student in students])


# In[ ]:




