# Database Management and Chatbot for Office Attendance

This document provides a detailed summary of the `gen_ai_dbms_1.py` Python file, which implements a simple office attendance tracking system using SQLite and a text-based chatbot interface. It covers database setup, data insertion, attendance querying, and natural language processing for query handling.

## 1. Database Setup and Initialization

The script begins by importing necessary libraries (`sqlite3` for database interaction, and `datetime`, `timedelta` for date calculations). It then establishes a connection to a local SQLite database named `office_data.db`. If the database file does not exist, SQLite automatically creates it.

* **Connection and Cursor:**
    ```python
    import sqlite3
    from datetime import datetime, timedelta

    conn = sqlite3.connect('office_data.db')
    cursor = conn.cursor()
    ```
* **Table Creation:** An `attendance` table is created within the database. This table stores attendance records with an auto-incrementing `id`, `name` of the person, and the `date` of attendance.
    ```sql
    CREATE TABLE IF NOT EXISTS attendance (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      date TEXT
    )
    ```
    This `CREATE TABLE` statement is executed to ensure the table exists before any data operations.

## 2. Sample Data Insertion

The script populates the `attendance` table with sample data for the current day, yesterday, and the day before yesterday. The number of attendees varies for each day to simulate different attendance counts.

* **Data Generation Logic:**
    * It iterates for 3 days, starting from `today`.
    * For each day, it inserts `100 + (day_index * 10)` records (e.g., 100 for today, 110 for yesterday, 120 for two days ago).
    * The `name` is formatted as "person_X", and the `date` is formatted as "YYYY-MM-DD".
    ```python
    today = datetime.now()
    for i in range(3):
      day = today - timedelta(days=i)
      for j in range(100 + i * 10):
        cursor.execute("INSERT INTO attendance(name, date) VALUES (?,?)",
                       (f"person_{j+1}", day.strftime("%Y-%m-%d")))
    conn.commit()
    conn.close() # Connection is closed after initial data insertion
    ```
* **Verification (Sample Read):** After insertion, the script re-connects to the database and fetches the first 5 rows from the `attendance` table to demonstrate the inserted data.
    ```python
    conn = sqlite3.connect('office_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance LIMIT 5")
    rows = cursor.fetchall()
    for row in rows:
      print(row)
    conn.commit()
    conn.close() # Connection is closed after verification
    ```

## 3. Core Function: `get_attendance_count`

This function is designed to query the database and return the total number of attendance records for a specified date string.

* **Function Definition:**
    ```python
    def get_attendance_count(date_str):
      conn = sqlite3.connect('office_data.db') # New connection for the function
      cursor = conn.cursor()
      cursor.execute("SELECT COUNT(*) FROM attendance WHERE date = ?", (date_str,))
      count = cursor.fetchone()[0]
      conn.commit()
      conn.close()
      return count
    ```
* **Example Usage:**
    ```python
    get_attendance_count('2025-07-20') # Example call
    ```
    *(Note: The exact output will depend on the current date when the script is run and how `today` is defined in the data insertion loop.)*

## 4. Initial Chatbot Handler (`handle_query`)

An early version of a chatbot handler is presented, capable of answering only about "yesterday's" attendance.

* **Limited Functionality:**
    ```python
    def handle_query(user_query):
      if 'yesterday' in user_query.lower():
        date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        count = get_attendance_count(date)
        return f"Bot: Yesterday, {count} people were in the office"
      else:
        return "Bot: Sorry, I can only answer about yesterday attendance right now"
    ```
* **Example Interaction:**
    ```python
    user_query = "How many people were in the office yesterday?"
    response = handle_query(user_query)
    print(response) # Example output: "Bot: Yesterday, 110 people were in the office" (count varies)
    ```

## 5. Enhanced Chatbot with Date Extraction (`chatbot_query_handler`)

This section introduces a more sophisticated chatbot capable of understanding "today", "yesterday", and specific date formats (YYYY-MM-DD) within user queries.

* **Regular Expression for Date Extraction:** The `re` module is used to find dates in the format `YYYY-MM-DD`.
    ```python
    import re
    re.search(r"\d{4}-\d{2}-\d{2}" , "How many people were in the office on 2025-07-19")
    re.search(r"\d{4}-\d{2}-\d{2}" , "How many people were in the office on 2025-07-19").group() # Extracts '2025-07-19'
    ```
* **`extract_date_from_query` Function:** This helper function parses the user query to determine the target date.
    * It checks for "today" and "yesterday" keywords.
    * If not found, it attempts to extract a `YYYY-MM-DD` date using a regular expression.
    * Returns `None` if no date is found or inferable.
    ```python
    def extract_date_from_query(user_query):
      today = datetime.now().date()
      if "today" in user_query.lower():
        return today.strftime("%Y-%m-%d")
      elif "yesterday" in user_query.lower():
        yesterday = today - timedelta(days=1)
        return yesterday.strftime("%Y-%m-%d")
      else:
        date_match = re.search(r"\d{4}-\d{2}-\d{2}" , user_query)
        if date_match:
          return date_match.group(0)
        return None
    ```
* **`chatbot_query_handler` Function:** This is the main chatbot function that integrates date extraction and database querying.
    * It calls `extract_date_from_query` to get the `target_date`.
    * If no `target_date` is found, it returns an error message.
    * Otherwise, it queries the `attendance` table for the count on `target_date`.
    * It returns an appropriate message indicating the attendance count or if no records are found for that date.
    ```python
    def chatbot_query_handler(user_query):
      conn = sqlite3.connect('office_data.db')
      cursor = conn.cursor()

      target_date = extract_date_from_query(user_query)
      if not target_date:
        return """Bot: Sorry I couldn't find the date in your query.
        Please try again using a valid date or words like 'today' or 'yesterday'"""

      cursor.execute("SELECT COUNT(*) FROM attendance WHERE date = ?", (target_date,))
      count = cursor.fetchone()[0]

      conn.commit()
      conn.close()

      if not count:
        return f"Bot: No attendance record found for {target_date}"
      else:
        return f"Bot: on {target_date}, {count} people were in the office"
    ```
* **Demonstration of Queries:** The script includes a loop to test the `chatbot_query_handler` with various predefined queries.
    ```python
    querries = [
        "How many people were in the office today?",
        "How many people were in the office on 2025-07-19?", # Example date, actual date depends on when script runs
        "How many people were in the office yesterday?",
        "Show me the attendance for 2025-07-18", # Example date
        "Show me the attendance for 2025-07-20", # Example date
        "What is attendance?" # Will trigger "couldn't find the date"
    ]
    for query in querries:
      print(f"User: {query}")
      response = chatbot_query_handler(query)
      print(f"{response}")
      print()
    ```
* **Interactive User Input:** The script concludes with a prompt for the user to enter a query, demonstrating real-time interaction with the chatbot.
    ```python
    user_input = input("What do you want to know? ")
    response = chatbot_query_handler(user_input)
    print(f"{response}")
    ```

## 6. Future Enhancements (Unimplemented Queries)

The file ends by listing two more complex queries that are not currently handled by the implemented `chatbot_query_handler`, indicating potential areas for future development:
* "Tell me about those employee who present yesterday but not today"
* "Difference in attendance count of last 3 days"
