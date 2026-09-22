# Lesson 03 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: First set of work in Lesson 3. The base code outlined in `lesson-03-query-data-with-select.md`, fully functional.
- Commit 2 hash + message:
- Optional Commit 3 hash + message:

## Run evidence
- Command run: `python SQLOnboarding-main/examples/lesson3_select.py`
- Terminal output pasted below:
```
Terence is in year 10, and their favourite subject is Software Engineering.
Leo is in year 11, and their favourite subject is PDHPE.
Awdsa is in year 7, and their favourite subject is Science.
Evelyn is in year 10, and their favourite subject is Software Engineering.
```

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output): I typed the changes into `lesson2_create_table.py` then ran both that and `lesson3_select.py`.

## Prediction before run
- Query version: SELECT name FROM students
- My prediction (rows/columns or sample output): 4 rows, with each students name
- What actually happened:
```
('Terence',)
('Leo',)
('Awdsa',)
('Evelyn',)
```

## SQL/Python changes I made
- Change 1: Changed the code to ensure the system would search for all variables.
- Change 2: Included the 'favourite_subject' variable in the output.
- Why these changes were mine (not just starter code): The 'favourite_subject' variable was not included in the starter code.

## Error and fix
- Error I hit: The system wasn't able to find variables other than name.
- How I fixed it: Changed `cursor.execute("SELECT name FROM students")` to `cursor.execute("SELECT name, year_group, favourite_subject FROM students")` =

## Understanding check (answer in your own words)
1. What is the job of `SELECT`?
2. What type of value does `fetchall()` return?
3. How did your output change when you selected fewer columns?

## Quality checklist
- [ ] Script runs without unhandled errors
- [ ] I included at least 2 lesson commits
- [ ] I included query output evidence
- [ ] I showed a prediction and compared it to actual output
- [ ] I made at least 2 personal changes to the starter work
- [ ] I answered all questions in my own words
