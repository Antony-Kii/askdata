# Week 2: AskData SQL Command-Line Tool

import sqlite3
from pathlib import Path

# Locate the Chinook database
database_path = Path.home() / "Desktop" / "DB" / "Chinook_Sqlite.sqlite"


# Function 1: Validate SQL input
def get_valid_query():
    while True:
        query = input("\nEnter a SQL query (or type exit): ").strip()

        if query.lower() == "exit":
            return None

        if query == "":
            print("Error: Query cannot be empty.")
            continue

        if not query.upper().startswith("SELECT "):
            print("Error: Please enter a SELECT query.")
            continue

        return query


# Function 2: Execute SQL query
def run_query(connection, query):
    try:
        cursor = connection.execute(query)

        # Get the column names
        columns = [item[0] for item in cursor.description]

        # Retrieve a maximum of 20 rows
        rows = cursor.fetchmany(20)

        print("\nColumns:", ", ".join(columns))

        for row in rows:
            print(" | ".join(str(value) for value in row))

        print("\nRows displayed:", len(rows))

    except sqlite3.Error as error:
        print("SQL Error:", error)


# Main program
def main():
    if not database_path.is_file():
        print("Error: Chinook database file not found.")
        print("Expected location:", database_path)
        return

    print("Welcome to AskData!")
    print("Query the Chinook music database.")
    print("Type exit to quit.")

    # Open the database in read-only mode
    connection = sqlite3.connect(
        database_path.as_uri() + "?mode=ro",
        uri=True
    )

    # Block database-changing SQL operations
    connection.execute("PRAGMA query_only = ON")

    try:
        while True:
            query = get_valid_query()

            if query is None:
                print("Goodbye!")
                break

            run_query(connection, query)

    finally:
        connection.close()


if __name__ == "__main__":
    main()
