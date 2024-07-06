#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sqlite3

def create_database():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    # Check if the table exists
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            dob TEXT,
            amount_due REAL
        )
    ''')
    conn.commit()
    conn.close()

create_database()


# In[ ]:




