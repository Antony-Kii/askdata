# Week 3: AskData SQL Results Analyzer

import sqlite3
from pathlib import Path
from collections import Counter

# Use the existing Chinook database
database_path = Path.home() / "Desktop" / "DB" / "Chinook_Sqlite.sqlite"


# Function 1: Validate SQL query
def get_valid_query():
    while True:
        query = input("\nEnter a SQL query (or type exit): ").strip()

        if query.lower() == "exit":
            return None

        if not query:
            print("Error: Query cannot be empty.")
            continue

        if not query.upper().startswith("SELECT "):
            print("Error: Please enter a SELECT query.")
            continue

        return query


# Function 2: Retrieve rows as dictionaries
def load_query_results(connection, query):
    cursor = connection.execute(query)

    # Extract column names
    columns = [item[0] for item in cursor.description]

    # Limit how many rows we analyze
    rows = cursor.fetchmany(100)

    # Convert tuples into dictionaries
    records = [dict(zip(columns, row)) for row in rows]

    return columns, records


# Function 3: Identify observed data types
def describe_type(values):
    types = {type(value).__name__ for value in values if value is not None}

    if not types:
        return "None / NULL"

    return ", ".join(sorted(types))


# Function 4: Analyze SQL results
def analyze_results(columns, records):
    summary = {
        "row_count": len(records),
        "column_count": len(columns),
        "columns": {}
    }

    for column in columns:
        values = [record[column] for record in records]

        # Find unique values
        unique_values = set(values)

        # Count occurrences of values
        counts = Counter(values)

        most_common = counts.most_common(1)

        summary["columns"][column] = {
            "data_types": describe_type(values),
            "unique_count": len(unique_values),
            "most_common": most_common[0] if most_common else None
        }

    return summary


# Function 5: Display analysis
def display_summary(summary):
    print("\n=== AskData SQL Analysis ===")

    print("Rows analyzed:", summary["row_count"])
    print("Columns:", summary["column_count"])

    for column, details in summary["columns"].items():
        print("\nColumn:", column)
        print("Observed types:", details["data_types"])
        print("Unique values:", details["unique_count"])
        print("Most common:", details["most_common"])


# Main program
def main():
    if not database_path.is_file():
        print("Error: Chinook database not found.")
        print("Expected:", database_path)
        return

    connection = sqlite3.connect(
        database_path.as_uri() + "?mode=ro",
        uri=True
    )

    connection.execute("PRAGMA query_only = ON")

    print("Welcome to AskData SQL Analyzer!")
    print("Type exit to quit.")

    try:
        while True:
            query = get_valid_query()

            if query is None:
                print("Goodbye!")
                break

            try:
                columns, records = load_query_results(connection, query)
                summary = analyze_results(columns, records)
                display_summary(summary)

            except (sqlite3.Error, TypeError, ValueError) as error:
                print("Query error:", error)

    finally:
        connection.close()


if __name__ == "__main__":
    main()
