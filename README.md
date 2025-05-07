# Birthday Organizer
## Purpose / Problem Statement
The Birthday Organizer is a simple, interactive Python program that helps users manage and reveal student birthdays while maintaining privacy. It addresses the need for a classroom-friendly tool that protects sensitive information unless specific criteria (e.g., knowing a student's favorite color) are met. This prevents accidental data exposure while making birthday lookups fun and engaging.

## Target Audience
This program is primarily designed for:

Teachers or classroom organizers managing student birthdays.

Students learning to code and build basic interactive Python apps.

Anyone interested in small-scale, privacy-conscious data lookup tools.

## Solution + Limitations
How it solves the problem:
Censors birthdays by default to protect privacy.

Only reveals birthday information when the correct favorite color is guessed.

Allows users to add new students to the organizer at any time.

Simple, menu-driven interface that works in any terminal.

## Limitations:
No option to delete or edit student entries.

Data is not saved between sessions (no file/database storage).

Only supports first-name lookup; duplicates or similar names could confuse results.

## Key Features / Key Components
Menu System: Offers four main options: view students, reveal birthday, add student, quit.

Censored View: Displays only first names with birthday hidden.

Guess Mechanic: Requires user to guess favorite color before revealing birthday.

Dynamic Addition: Users can add new full names, birthdays, and favorite colors.

## Technical Challenges + Future Plans
Challenges:
Matching first names reliably when full names are stored.

Ensuring input handling is user-friendly without external libraries.

Keeping the program readable and functional without adding extra complexity.

Future Plans:
Add file saving/loading so student data persists across sessions.

Implement student deletion and editing options.

Improve name matching (e.g., support last names or nicknames).

## Project Timeline
Before I began this project, I brainstormed: How could I solve an issue in my current workplace?
The project started as a game without any user data storage, but due to requirements, I had to change it and add a section where the user could input their information to enjoy the program, with the focus still being on user data collection.

## Tools and Resources Used
Python – Programming language used.

ChatGPT (OpenAI) – Used to brainstorm and generate random data, debug, and help document.

Python Docs – For understanding string, list, and input functions.

