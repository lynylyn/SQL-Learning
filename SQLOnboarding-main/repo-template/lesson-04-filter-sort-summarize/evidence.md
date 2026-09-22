# Lesson 04 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: b8d98a5 - First set of work in Lesson 3. The base code outlined in `lesson-04-filter-sort-summarize.md`, slightly edited according to the activity, fully functional.
- Commit 2 hash + message: f5fab5f - Completed the stretch challenge and added my own additions to the code.
- Optional Commit 3 hash + message: Answered all questions and marked off the quality checklist.

## Run evidence
- Command run: python SQLOnboarding-main/examples/lesson4_filter.py
- Terminal output pasted below:

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
    - Changed `year_group = 10` to `year_group = 11`

## Prediction before run
- Query version: COUNT(*)
- My prediction (filtered rows, order, or count): 4
- What actually happened: 4

## SQL/Python changes I made
- Change 1: Edited the code so the year group would be displayed before the name.
- Change 2: Changed the formatting of the output to enhance readability.
- Why these changes were mine (not just starter code): The output was not formatted at all in the code given.

## Error and fix
- Error I hit: The f string would not work.
- How I fixed it: Changed `for row in rows` to `for year_group, name in rows`

## Understanding check (answer in your own words)
1. What does `WHERE` do?
    - `WHERE` filters the rows so only rows with a certain value will be output.
2. Why is `?` used in the query?
    - `?` is used to represent the defined value of `year_group`.
3. What does `COUNT(*)` tell you in this lesson?
    - `COUNT(*)` tells us the number of matching rows.

## Quality checklist
- [x] Script runs without unhandled errors
- [x] I included at least 2 lesson commits
- [x] I included filtered/sorted summary evidence
- [x] I showed a prediction and compared it to actual output
- [x] I made at least 2 personal changes to the starter work
- [x] I answered all questions in my own words
