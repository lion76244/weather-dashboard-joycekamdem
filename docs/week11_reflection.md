🔖 Section 0: Fellow Details
Fill out the table below:

Field	Your Entry
Name: Joyce Kamdem	
GitHub Username:	lion76244
Preferred Feature Track	Data / Visual / Interactive / Smart: Simple Statistics, Trend detection, Weather History Tracker
Team Interest	Yes / No — If Yes: N/A

✍️ Section 1: Week 11 Reflection
Answer each prompt with 3–5 bullet points:

Key Takeaways: What did you learn about capstone goals and expectations?: 

Concept Connections: Which Week 1–10 skills feel strongest? Which need more practice?:

Early Challenges: Any blockers (e.g., API keys, folder setup)?:

Support Strategies: Which office hours or resources can help you move forward?:
- Afsana walking me through how to do each point was very helpful

🧠 Section 2: Feature Selection Rationale
List three features + one enhancement you plan to build.

#	Feature Name	Difficulty (1–3)	Why You Chose It / Learning Goal
1 Simple Statistics 
2 Trend detection
3 Weather History Tracker	
Enhancement	–	Creative Visuals – Use canvas animations, emojis, or styled graphics for flair
🧩 Tip: Pick at least one “level 3” feature to stretch your skills!


🗂️ Section 3: High-Level Architecture Sketch
Add a diagram or a brief outline that shows:

Core modules and folders
main.py
api.py
config.py
gui.py
data
    --database.csv
    --data_collection.py
docs
    --week11_reflection.md
    --readme.md

Feature modules
    --Simple_Statistics.py
    --Trend_detection.py
    --Weather_History_Tracker.py

Data flow between components
main.py calls-- gui.py
gui.py calls -- api.py
gui.py calls -- --Simple_Statistics.py 
                        --relies on api.py
                --data_collection.py
                    --relies on api.py
                --Trend_detection.py
                    --relies on api.py
                    --relies on data_collection.py
                --Weather_History_Tracker.py
                        --relies on api.py
                        --relies on data_collection.py

📊 Section 4: Data Model Plan
Fill in your planned data files or tables:

File/Table Name	Format (txt, json, csv, other)	Example Row
database.csv	csv	2025-06-09,New Brunswick,78,Sunny

📆 Section 5: Personal Project Timeline (Weeks 12–17)
Customize based on your availability:

Week	Monday	Tuesday	Wednesday	Thursday	Key Milestone
12	API setup	Error handling	Tkinter shell	Buffer day	Basic working app
13	Feature 1			Integrate	Feature 1 complete
14	Feature 2 start		Review & test	Finish	Feature 2 complete
15	Feature 3	Polish UI	Error passing	Refactor	All features complete
16	Enhancement	Docs	Tests	Packaging	Ready-to-ship app
17	Rehearse	Buffer	Showcase	–	Demo Day

⚠️ Section 6: Risk Assessment
Identify at least 3 potential risks and how you’ll handle them.
My Api does not connect with the key -- troubleshoot the key or revert
my gui is not linking correctly --check the code and errors 
my main gets messed up --revert to an old version 

Risk	Likelihood (High/Med/Low)	Impact (High/Med/Low)	Mitigation Plan
API Rate Limit	Medium	Medium	Add delays or cache recent results

🤝 Section 7: Support Requests
What specific help will you ask for in office hours or on Slack?
I will ask for breakdown on the errors I am having, and check-ins for progress.

✅ Section 8: Before Monday (Start of Week 12)
Complete these setup steps before Monday:

Push main.py, config.py, and a /data/ folder to your repo

Add OpenWeatherMap key to .env (⚠️ Do not commit the key)

Create files for the chosen feature in /features/ 

like this:
# weather_journal.py
"""
Feature: Weather Journal
- Stores daily mood and notes alongside weather data
"""
def add_journal_entry(date, mood, notes):
    # your code goes here
    pass
Commit and push a first-draft README.md

Book office hours if you're still stuck on API setup
 
 📤 Final Submission Checklist:
✅ Week11_Reflection.md completed
✅ File uploaded to GitHub repo /docs/
✅ Repo link submitted on Canvas

📈 2. Weather Trend Logger
📊 What it does: Every time a user requests the weather, store the city, date, and temperature in a local JSON or CSV file.

🧠 Cool factor: Over time, build a personal weather history for any city they searched.

💡 Bonus: Add a plot of their city’s weather changes across days.

--look at week 8 after class asignment