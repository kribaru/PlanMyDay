# PlanMyDay
This app is designed to assist users with time management and organization by creating a schedule that accounts for a variety of needs.

# How to Run

Disclaimer: at the moment, this app is still in early stages of development, and the app is not fully functional. 

## Backend
  1. Create venv in VSCode Terminal. 
  2. Run Python code. 
  3. Click the link to where the 
# Project Abstract
This document proposes an app designed to assist users with organization and time management. For people who struggle with executive dysfunction or have trouble budgeting time, it can be difficult to determine how to optimize schedules in a way that promotes efficiency without sacrificing mental or physical health. This app aims to alleviate instances of indecision or functional freeze by designing a calendar for the user each day. 

Users can input their weekly responsibilities and commitments, or they can add links to calendars from other apps. Every morning, the app designs a schedule that takes into account preparation time, travel time, rest, health and wellness, and future projects to be completed. 
scheduler

## Conceptual Design
Describe with text (and maybe UML diagrams) the initial design concept. Include hardware and software architecture, operating system, programming language, framework, libraries, APIs, etc.

The app will be created using Python in the backend and JavaScript, HTML, and CSS in the frontend.  

## Class Diagram
<img width="718" alt="Screenshot 2025-05-07 at 12 04 31 AM" src="https://github.com/user-attachments/assets/28dc6052-2500-4b98-bda9-07738410adc7" />

## Sequence Diagram
This sequence diagram depicts what happens when a user has added a commitment to meet a friend. The user has scheduled a meeting with a friend at Reading Terminal Market at 5:30 pm. The app determines travel time using information from a map application, how early a user needs to start getting ready, and what they need to bring to their meeting (like keys, wallet, and other user-inputted items). 

<img width="627" alt="Screenshot 2025-05-06 at 11 44 45 PM" src="https://github.com/user-attachments/assets/b9d13f77-409f-4e84-b466-705294b58991" />

## Background
Time management apps are not a new creation, and many apps, like Google Calendar, Notion, and Calendly, have tried to find solutions. These applications offer tools such as calendar syncing, reminders, task organization, and goal tracking, but they lack the more personal aspect that can allow the application to be more useful outside of professional settings. This project is designed to incorporate solutions in multiple aspects of life, including social commitments, hobbies, and wellness. 

Some functionalities include:
- Travel time calculation: when a user inputs their schedule, if they have an event or commitment, the app determines how early they should leave in order to reach their location on time
- Reminders: The app provides reminders throughout the day in order to help the user reach their goals. 
  - Eat: based on the schedule and user input regarding their typical nutrition plans and preferences, the app can plan meals accordingly and send reminders. 
  - Work: user can input their commitments, like assignments, projects, personal goals, etc, and the app will map out time in the schedule for the user to make progress. Based on these timings, the app will send reminders for when the user should start working and how much time they must commit
  - Rest: Based on the amount of work done per day, and based on user preferences, the app calculates when and how long the user can rest. Rest segments would be time for the user to do any activity they choose. 


