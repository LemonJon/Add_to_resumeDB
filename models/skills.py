def insert_skill(connection, record):
    query = """
    INSERT INTO skills (skill_name, skill_type, skill_level)
    VALUES (%s, %s, %s)
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, record)
        connection.commit()
        print("Skill record added successfully")
    except Error as e:
        print(f"Failed to insert skill: {e}")