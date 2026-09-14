# Lesson 01 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: 6705cb7 - First set of work in Lesson 1. The base code outlined in `lesson-01-setup-and-first-connection.md`, fully functional.
- Commit 2 hash + message: Extended on the original code with the 'Stretch Challenge'. Ensured all exit questions were answered.
- Optional Commit 3 hash + message:

## Run evidence
- Command run (example: `python lesson1_connect.py`):

    `python SQLOnboarding-main/examples/lesson1_connect.py`
- Terminal output pasted below:
    ```
    PS C:\Users\evech\Documents\GitHub\SQL-Learning> python SQLOnboarding-main/examples/lesson1_connect.py
    Database connected!
    Database closed!
    PS C:\Users\evech\Documents\GitHub\SQL-Learning>
    ```

## What I changed from the starter example
- I changed the database name to 'library.db' and added an extra 'print' line.

## Error and fix
- Error I hit: The code would not run in the terminal.
- How I fixed it: I had to connect to the internet and ensure all folder names were in the command.

## Understanding check (answer in your own words)
1. What is the difference between Python and SQLite?
    - SQLite is a library within Python that provides an SQL-like interface to read, query, and write SQL databases.
2. What file was created when the script ran?
    - The file `library.db` (originally    `school.db`) was created.
3. What does the connection do?
    - The connection ensures that the database exists and, if it doesn't, it ensures it has been created.

## Quality checklist
- [x] Script runs without unhandled errors
- [x] I included at least 2 lesson commits
- [x] I included terminal evidence
- [x] I answered all questions in my own words
