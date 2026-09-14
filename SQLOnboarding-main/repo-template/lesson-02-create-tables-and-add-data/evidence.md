# Lesson 02 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: 2d1806d - First set of work in Lesson 2. The base code outlined in `lesson-02-create-tables-and-add-data.md`, fully functional.
- Commit 2 hash + message: 04f0106 - Built on top of the base work in Lesson 2, enhancing my understanding by answering questions and renaming some of the data.
- Optional Commit 3 hash + message: Did the 'Stretch Challenge' and completed all questions.

## Run evidence
- Command run: `python SQLOnboarding-main/examples/lesson2_create_table.py`
- Terminal output pasted below:
    None, but ran without error

## SQL/Python changes I made
- I added a new row, column, and changed some of the data in the table.

## Error and fix
- Error I hit: The system couldn't add a new column to the table.
- How I fixed it: Deleted `library.db` and re-ran the code.

## Understanding check (answer in your own words)
1. Why do we use `commit()`?
    - commit() pushes the changes to the database.
2. What does `PRIMARY KEY` mean?
    - The primary key is a unique identifier for each row in a table.
3. Why is `IF NOT EXISTS` useful when creating tables?
    - IF NOT EXISTS ensures that a table has been created and the system isn't attempting to feed data into an empty database.

## Quality checklist
- [x] Script runs without unhandled errors
- [x] I included at least 2 lesson commits
- [x] I showed inserts and saved changes
- [x] I answered all questions in my own words
