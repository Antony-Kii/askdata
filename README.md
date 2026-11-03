# askdata
AI engineering learning project for Python, SQL, data analysis, and AI applications
# AskData — AI Engineering Learning Project

## Project Overview
AskData is my hands-on project for learning Python, SQL, data analysis, and AI engineering.

## Week 1 — Python and SQL Foundations

### Chinook Sample Database
I downloaded and explored the Chinook SQLite sample database using DB Browser for SQLite.

**Source:** https://github.com/lerocha/chinook-database

### Five Tables Identified
1. Album — Music albums
2. Artist — Musicians and bands
3. Customer — Customer records
4. Invoice — Customer purchases
5. Track — Individual music tracks

### Tools Used
- Python
- Visual Studio Code
- GitHub Desktop
- DB Browser for SQLite

### Learning Goals
- Learn Python fundamentals
- Understand relational databases
- Practice SQL queries
- Develop AI engineering skills

## Week 3 — Python Collections and Data Analysis

Completed Python exercises covering lists, dictionaries, sets, and comprehensions.

### CSV Record Analyzer
Built `csv_analyzer.py` to read and analyze a synthetic music sales dataset. Features include record counting, sales totals, unique genre identification, and frequency analysis.

### AskData SQL Results Analyzer
Built `askdata_analysis.py` to analyze results from the Chinook SQLite database.

Features:
- Read-only SQL query execution
- Conversion of SQL rows into Python dictionaries
- Row and column summaries
- Observed data type identification
- Unique-value counts and frequency analysis
- Basic query validation and SQL error handling
- Analysis of up to 100 retrieved rows per query

**Database source:** https://github.com/lerocha/chinook-database

**Setup:** Download the Chinook SQLite database and update the `database_path` variable in `askdata_analysis.py` to match its location on your computer.
