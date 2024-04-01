def update_database_settings(db_config, save_db_config):
    print("Update database settings. Press enter to keep current value.")

    new_host = input(f"New Host (current: {db_config['host']}): ")
    new_user = input(f"New User (current: {db_config['user']}): ")
    new_database = input(f"New Database Name (current: {db_config['database']}): ")

    if new_host:
        db_config['host'] = new_host
    if new_user:
        db_config['user'] = new_user
    if new_database:
        db_config['database'] = new_database

    # Save the updated settings back to the JSON file
    save_db_config(db_config)
    print("Database settings updated.")