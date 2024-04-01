from db.db_connection import get_db_connection
from models import education, skills, work_experience
from models.db_settings import update_database_settings
import json
import getpass
import os


db_config = {
        'host': None,
        'user': None,
        'passwd': None, 
        'database': None
    }

config_file = 'db_config.json'

def save_db_config(config):
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)

def load_db_config():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    else:
        return None
    
def prompt_password():
    db_password = getpass.getpass("Database Password: ")
    db_config['passwd'] = db_password

def prompt_database_settings():
    print("Enter databas settings:")
    db_config['host'] = input("Host: ")
    db_config['user'] = input("User: ")
    db_config['database'] = input("Database name: ")

def main_menu():
    print("1: Add Work Experience")
    print("2: Add Education Record")
    print("3: Add Skill")
    print("4: Change Database Settings")
    print("5: Quit")
    choice = input("Choose an option: ")
    return choice

def main():
    global db_config

    loaded_config = load_db_config()

    # Check if database settings are not set and prompt for them
    if loaded_config is not None:
        db_config.update(loaded_config)
    else:
        prompt_database_settings()
        save_db_config(db_config)

    #prompt for password
    prompt_password()

    # Connect to the database
    connection = get_db_connection(db_config)


    if connection:
        while True:
            choice = main_menu()

            if choice == '1':
                title = input("Enter job title: ")
                company = input("Enter company name: ")
                from_date = input("Enter start date (YYYY-MM-DD): ")
                to_date = input("Enter end date (YYYY-MM-DD) or leave blank if current: ")
                body = input("Enter job description: ")
                data = (title, company, from_date, to_date, body)
                work_experience.insert_work_experience(connection, data)
            elif choice == '2':
                title = input("Enter degree title: ")
                university = input("Enter university name: ")
                city = input("Enter city: ")
                from_date = input("Enter start date (YYYY-MM-DD): ")
                to_date = input("Enter end date (YYYY-MM-DD) or leave blank if current: ")
                body = input("Enter description: ")
                data = (title, university, city, from_date, to_date, body)
                education.insert_education_record(connection, data)
            elif choice == '3':
                skill_name = input("Enter skill name: ")
                skill_type = input("Enter skill type (e.g., Technical, Soft): ")
                skill_level = input("Enter skill level (e.g., Beginner, Intermediate, Expert): ")
                data = (skill_name, skill_type, skill_level)
                skills.insert_skill(connection, data)
            elif choice == "4":
                update_database_settings(db_config, save_db_config)
                prompt_password()
                continue
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

            if input("Continue? (y/n): ").lower() != 'y':
                break

        connection.close()

if __name__ == "__main__":
    main()