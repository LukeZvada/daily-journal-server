from models.entries import Entries
import sqlite3
import json


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.date,
            e.concept,
            e.entry,
            e.id,
            e.mood_id
        FROM entries e
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert datas of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for data in dataset:
            entry = Entries(data['date'], data['concept'], data['entry'],
                            data['id'], data['mood_id'])

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.date,
            e.concept,
            e.entry,
            e.id,
            e.mood_id
        FROM entries e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        entries = Entries(data['date'], data['concept'], data['entry'], data['id'], data['mood_id'])

        return json.dumps(entries.__dict__)