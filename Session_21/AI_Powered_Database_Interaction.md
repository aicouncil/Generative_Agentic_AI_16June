# AI-Powered Database Interaction: A Smart Chatbot for Attendance Records

This document provides a detailed explanation of the `gen_ai_dbms_2.py` script, which demonstrates a sophisticated approach to interacting with a SQLite database using a Generative AI model (Gemini) to interpret natural language queries and convert them into executable SQL. This builds upon the basic database operations and local query handling seen in previous iterations by integrating Large Language Model (LLM) capabilities.

## 1. Initial Database Setup and Data Seeding

The script begins by establishing a connection to a local SQLite database and setting up an `attendance` table, similar to `gen_ai_dbms_1.py`.

* **Database Connection:** Connects to `office_data.db`, creating it if it doesn't exist.
    ```python
    import sqlite3
    from datetime import datetime, timedelta

    conn = sqlite3.connect('office_data.db')
    cursor = conn.cursor()
    ```
* **Table Creation:** Creates an `attendance` table with `id` (primary key, autoincrement), `name` (text), and `date` (text in YYYY-MM-DD format) columns.
    ```sql
    CREATE TABLE IF NOT EXISTS attendance (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      date TEXT
    )
    ```
* **Sample Data Insertion:** Populates the `attendance` table with attendance records for the current day, yesterday, and the day before yesterday. The number of records for each day is dynamically set (100, 110, 120 respectively).
    ```python
    today = datetime.now()
    for i in range(3):
      day = today - timedelta(days=i)
      for j in range(100 + i * 10):
        cursor.execute("INSERT INTO attendance(name,date) VALUES (?,?)", (f"person_{j+1}" , day.strftime("%Y-%m-%d")))
    conn.commit()
    conn.close()
    ```
* **Initial Data Verification:** A quick read of the first 5 rows confirms data insertion.
    ```python
    conn = sqlite3.connect('office_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance LIMIT 5")
    rows = cursor.fetchall()
    for row in rows:
      print(row)
    conn.commit()
    conn.close()
    ```

## 2. Gemini API Integration

The core enhancement in this script is the integration of Google's Generative AI model (Gemini) to enable natural language to SQL query generation.

* **API Configuration:** The `google.generativeai` library is imported, and the Gemini API key is configured using `userdata.get('GEMINI_API_KEY')`.
    ```python
    import google.generativeai as genai
    from google.colab import userdata

    genai.configure(api_key = userdata.get('GEMINI_API_KEY'))
    ```
* **Model Instantiation:** The `gemini-2.5-flash` model is chosen for generating content.
    ```python
    gemini_model = genai.GenerativeModel('models/gemini-2.5-flash')
    ```

## 3. Advanced Chatbot Query Handler (`chatbot_query_handler` - Iterations)

The script presents a refined `chatbot_query_handler` function through several iterations, demonstrating progressive improvements in its capabilities.

### 3.1. Iteration 1: SQL Query Generation (without execution)

This first version of the enhanced handler focuses solely on demonstrating the Gemini model's ability to generate appropriate SQLite SQL queries based on user's natural language input.

* **Prompt Engineering:** A crucial aspect is the detailed `prompt` provided to the Gemini model. This `prompt` instructs the AI on the database schema (`attendance` table with `id`, `name`, `date`), expected date format (`YYYY-MM-DD`), and provides examples of desired SQL for various query types (e.g., `COUNT`, `EXCEPT` for comparisons, `FILTER` by name).
    ```python
    prompt = f"""
    Based on the following user query, Generate a SQLite SQL query to reterive information from the 'attendance' table.
    The 'attendance' table has columns 'id' (integer), 'name' (text), 'date' (text).
    The date format in the table is 'YYYY-MM-DD'.
    For example, If the user asks 'How many people were in the office yesterday?', the SQL query should be:
    SELECT count(*) from attendance where date = 'YYYY-MM-DD_for_yesterday'
    Replace 'YYYY-MM-DD_for_yesterday' with the actual date for yesterday.
    If the user asks for employees present on one day but not another, use a query with EXCEPT.
    If the user asks for attendance of a specific person, filter by name.
    You need to generate appropriate prompt based on user query that can be provide the result user is expecting from the 'attendance' table.

    User query : {user_query}
    """
    ```
* **SQL Generation and Cleaning:** The Gemini model generates a response, which is then extracted and cleaned by removing "sqlite" and markdown code block fences (` ``` `).
* **Error Handling:** A `try-except` block is used to catch potential errors during SQL generation with Gemini.
* **Output:** This iteration only prints the generated SQL query.
    ```python
    # Example queries and their generated SQL output (actual date will vary)
    # User: How many people were in the office today?
    # Generated SQL: SELECT count(*) FROM attendance WHERE date = '2025-07-23'
    # User: Tell me about those employees who present yesterday but not today
    # Generated SQL: SELECT name FROM attendance WHERE date = '2025-07-22' EXCEPT SELECT name FROM attendance WHERE date = '2025-07-23'
    ```

### 3.2. Iteration 2: SQL Query Generation and Execution

Building on the previous version, this iteration enhances the `chatbot_query_handler` to not only generate the SQL query but also execute it against the SQLite database.

* **Execution and Result Retrieval:** After generating the SQL (`generate_sql`), `cursor.execute(generate_sql)` runs the query, and `cursor.fetchall()` retrieves all results.
* **Return Value:** This version returns both the `result` (the fetched rows) and the `len(result)` (number of rows).
    ```python
    # Example queries and their actual execution results
    # User: How many people were in the office today?
    # ((100,), 1)
    # User: Attendance report of person_101
    # ([('person_101', '2025-07-23'), ('person_101', '2025-07-22'), ('person_101', '2025-07-21')], 3)
    ```

### 3.3. Iteration 3: SQL Query Generation, Execution, and Formatted Output

The final iteration refines the `chatbot_query_handler` further by providing more user-friendly output formatting based on the nature of the query result.

* **Output Formatting Logic:**
    * If `len(result) == 0`: Returns "No Information".
    * If `len(result) > 1`: Returns the raw `result` list (e.g., for lists of names).
    * If `len(result) == 1`: Returns the first element of the single-row `result` (e.g., for a count).
* **Interactive Chatbot Loop:** The script concludes with a demonstration loop of predefined queries and an interactive input prompt for the user to test the fully functional chatbot.
    ```python
    # Example of formatted output for various queries
    # User: How many people were in the office today?
    # Generated SQL: SELECT count(*) FROM attendance WHERE date = '2025-07-23'
    # (100,)
    # User: Show me the attendance for '2025-07-18'
    # Generated SQL: SELECT * FROM attendance WHERE date = '2025-07-18'
    # No Information
    # User: Tell me about those employees who present yesterday but not today
    # Generated SQL: SELECT name FROM attendance WHERE date = '2025-07-22' EXCEPT SELECT name FROM attendance WHERE date = '2025-07-23'
    # [('person_101',), ('person_102',), ...] (list of names)
    # User: What do you want to know? (interactive input)
    ```

## 4. Key Concepts Illustrated

* **Text-to-SQL (Natural Language to SQL):** The core capability demonstrated, where natural language questions are converted into structured SQL queries by a generative AI model.
* **Generative AI (LLM):** Specifically, the Gemini model's role in understanding context, table schema, and intent to produce correct SQL.
* **Prompt Engineering:** The careful crafting of instructions to guide the LLM's output towards desired SQL syntax and logic.
* **Database Interaction (SQLite):** Fundamental operations like connecting, creating tables, inserting data, and executing queries (`SELECT`, `COUNT`, `EXCEPT`) are shown.
* **Dynamic Query Generation:** The ability to generate SQL queries on-the-fly based on varied user input, making the system highly flexible.
* **Error Handling:** Implementation of `try-except` blocks to manage potential issues during AI interaction or database operations.
