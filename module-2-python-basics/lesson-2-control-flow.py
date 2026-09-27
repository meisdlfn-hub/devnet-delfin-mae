"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Delfin, Cherrie Mae S.
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow allows a program to decide what to do based on a condition. 
The if, elif, and else statements are used to check different conditions and choose which part of the code should run.

============================================
KEY VOCABULARY
============================================
- condition: A statement that is checked to see if it is True or False.
- if / elif / else: Statements used to choose what code will run based on a condition.
- comparison operator: A symbol used to compare two values, such as ==, >, <, >=, or <=.
- boolean expression: An expression that results in either True or False.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

age = 20

if age >= 18:
print("You can register.")
elif age >= 13:
print("You need permission.")
else:
print("You are too young to register.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

One mistake I want to avoid is forgetting the colon after an if, elif, or else statement. 
I also learned that the code inside the condition needs to be properly indented so Python knows which statements belong to it.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]

Control flow is useful when a program needs to make decisions. 
For example, a bar can use conditions to check a customer's age and decide if they are allowed to enter.
"""
