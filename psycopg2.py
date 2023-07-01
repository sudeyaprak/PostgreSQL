#Creating type 'academic_titles'
new_type = '''
      CREATE TYPE academic_titles as ENUM (
          'Prof.','Assoc. Prof.', 'Asst. Prof', 'Res. Asst.', 'Lect.')'''
cursor.execute(new_type)
"

import psycopg2

#Establishing the connection
conn = psycopg2.connect(database = "odev", user = "postgres", password = "12345", host = "localhost", port = "5432")

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Droping table if already exists.
cursor.execute("DROP TABLE IF EXISTS ACADEMICS")
cursor.execute("DROP TABLE IF EXISTS COURSES")
cursor.execute("DROP TABLE IF EXISTS DELIVERED_BY")

#Creating table as per requirement
academics ='''
      CREATE TABLE academics (
          id_ VARCHAR(4) PRIMARY KEY NOT NULL,
          name_surname VARCHAR(50) NOT NULL,
          title ACADEMIC_TITLES NOT NULL
      )'''
courses = '''
      CREATE TABLE courses (
          id_ CHARACTER(6) PRIMARY KEY NOT NULL,
          name VARCHAR(50) NOT NULL,
          akts INTEGER NOT NULL
      )'''
delivered_by = '''
      CREATE TABLE delivered_by (
          id_courses CHARACTER(6) PRIMARY KEY NOT NULL,
          id_academics VARCHAR(4) NOT NULL,
          CONSTRAINT fk_idcourse
              FOREIGN KEY(id_courses)
                 REFERENCES courses(id_)
                 ON DELETE SET NULL,
          CONSTRAINT fk_idacademic
              FOREIGN KEY(id_academics)
                 REFERENCES academics(id_)
                 ON DELETE SET NULL
      )''' 

cursor.execute(academics)
print("Academics Table created successfully........")
cursor.execute(courses)
print("Courses Table created successfully........")
cursor.execute(delivered_by)
print("Delivered_by Table created successfully........")

conn.commit()
#Closing the connection
conn.close()

#Adding layers
insert = input("Add a new layer(y/n):")
if insert == 'y':
    
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="12345",
                                  host="localhost",
                                  port="5432",
                                  database="odev")
        cursor = connection.cursor()
    
        which_table = input("Which table do you want to insert(academics/courses/delivered_by):")
        if which_table == 'academics':
            id_ = input("Lecturer ID:")
            name_surname = input("Lecturer Name Surname:")
            title = input("Lecturer Title:")
            postgres_insert_query = """ INSERT INTO academics (id_, name_surname, title) VALUES (%s,%s,%s)"""
            record_to_insert = (id_, name_surname, title)
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into academics table")
        
        elif which_table == 'courses':
            id_ = input("Course No:")
            name = input("Course Name:")
            akts = int(input("Course Akts:"))
            postgres_insert_query = """ INSERT INTO courses (id_, name, akts) VALUES (%s,%s,%s)"""
            record_to_insert = (id_, name, akts)
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into courses table")
        
        elif which_table == 'delivered_by':
            id_courses = input("Course No:")
            id_academics = input("Lecturer ID:")
            postgres_insert_query = """ INSERT INTO delivered_by (id_courses, id_academics) VALUES (%s,%s)"""
            record_to_insert = (id_courses, id_academics)
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into delivered_by table")
        
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)

else:
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")   
