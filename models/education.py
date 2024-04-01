def insert_education_record(connection, record):
    query = """
    INSERT INTO education (title, university, city, from_date, to_date, body)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, record)
        connection.commit()
        print("Education record added successfully")
    except Error as e:
        print(f"Failed to insert record: {e}")