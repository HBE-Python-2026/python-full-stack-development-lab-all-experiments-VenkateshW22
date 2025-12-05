# Experiment 6: MySQL Database Operations
import mysql.connector
from mysql.connector import Error

def run_db_operations():
    connection = None
    cursor = None
    try:

    # 1. Connect to Database
    # TODO: Create a connection object to 'company_db' using mysql.connector.connect()
    # TODO: Create a cursor object

    # 2. Create Table
    # TODO: Execute SQL query to CREATE TABLE 'employees' (id, name, position)

    # 3. Insert Data
    # TODO: Execute SQL query to INSERT two employees ("Alice Smith", "Bob Johnson")
    # TODO: Commit the transaction (connection.commit())

    # 4. Select Data
    # TODO: Execute SELECT * FROM employees
    # TODO: Fetch all rows and print them

    # 5. Update Data
    # TODO: Execute UPDATE query to change Alice's position
    # TODO: Commit the transaction

    # 6. Delete Data
    # TODO: Execute DELETE query to remove Bob
    # TODO: Commit the transaction

    except Error as e:
        print(f"Error: {e}")
    finally:
        # TODO: Close the cursor and connection if they exist
        pass

if __name__ == "__main__":
    run_db_operations()