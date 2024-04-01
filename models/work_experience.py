def insert_work_experience(connection, record):
    query = """
    INSERT INTO work_experience (title, company, from_date, to_date, body)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, record)
        connection.commit()
        print("Work experience added successfully")
    except Error as e:
        print(f"Failed to add work experience {e}")