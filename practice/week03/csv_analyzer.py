# Week 3: CSV Record Analyzer
# AskData AI Engineering Project

import csv
from pathlib import Path
from collections import Counter

# Locate the CSV file in the same folder
csv_path = Path(__file__).parent / "music_sales.csv"


# Function 1: Load CSV records
def load_csv(file_path):
    records = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    return records


# Function 2: Analyze the records
def analyze_sales(records):

    # Count total records
    total_records = len(records)

    # Convert sales from text to integers
    sales_values = [int(row["Sales"]) for row in records]

    # Calculate total sales
    total_sales = sum(sales_values)

    # Identify unique genres
    unique_genres = {row["Genre"] for row in records}

    # Count how often each genre appears
    genre_counts = Counter(row["Genre"] for row in records)

    # Identify most common genre
    most_common_genre = genre_counts.most_common(1)[0]

    return {
        "total_records": total_records,
        "total_sales": total_sales,
        "unique_genres": unique_genres,
        "genre_counts": genre_counts,
        "most_common_genre": most_common_genre
    }


# Function 3: Display the summary
def display_summary(summary):

    print("\n=== AskData CSV Analysis ===")

    print("Total records:", summary["total_records"])
    print("Total sales:", summary["total_sales"])

    print("Unique genres:", sorted(summary["unique_genres"]))

    print("\nGenre counts:")

    for genre, count in sorted(summary["genre_counts"].items()):
        print(genre, ":", count)

    print("\nMost common genre:", summary["most_common_genre"][0])
    print("Number of records:", summary["most_common_genre"][1])


# Main program
def main():

    if not csv_path.is_file():
        print("Error: CSV file not found.")
        return

    try:
        records = load_csv(csv_path)

        if not records:
            print("Error: CSV file contains no records.")
            return

        summary = analyze_sales(records)

        display_summary(summary)

    except (OSError, ValueError, KeyError) as error:
        print("Error analyzing CSV:", error)


if __name__ == "__main__":
    main()
