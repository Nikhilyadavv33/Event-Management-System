import sqlite3
import csv

# Connect to your Flask database
conn = sqlite3.connect('event.db')
cursor = conn.cursor()

# Create table if not exists (same as in your Flask app)
cursor.execute('''
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY,
    event_name TEXT,
    event_date TEXT,
    venue_id INTEGER
)
''')

# Read CSV and insert data
with open('Events.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO events (event_id, event_name, event_date, venue_id)
            VALUES (?, ?, ?, ?)
        ''', (
            row['event_id'],
            row['event_name'],
            row['event_date'],
            row['venue_id']
        ))

conn.commit()
conn.close()

print("✅ Data imported successfully into event.db!")
