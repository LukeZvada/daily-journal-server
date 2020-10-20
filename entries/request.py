import Moods
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


def create_entry(newEntry):
	with sqlite3.connect("./dailyjournal.db") as conn:
		db_cursor = conn.cursor()
		db_cursor.execute("""
		INSERT INTO Entries
			( date, concept, entry, mood_id )
		VALUES
			( ?, ?, ?, ? );
		""" , (newEntry['date'], newEntry['concept'], newEntry['entry'], newEntry['moodId']) )

		id = db_cursor.lastrowid
		newEntry['id'] = id

	return json.dumps(newEntry)

def entry_search (concept):
    with sqlite3.connect('./dailyjournal.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(f"""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date
        FROM Journal_entries e
        WHERE e.entry LIKE '%{concept}%'
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entries(row['id'], row['concept'], row['entry'], row['mood_id'],
                                    row['date'])
            entries.append(entry.__dict__)

        return json.dumps(entries)

def delete_entry(entryId):
	with sqlite3.connect("./dailyjournal.db") as conn:
		db_cursor = conn.cursor()
		
		db_cursor.execute("""
		DELETE 
		FROM Entries AS e
		WHERE e.id = ?
		""", ( entryId, ))

		db_cursor.execute("""
		DELETE 
		FROM EntryTags AS et
		WHERE et.entry_id = ?
		""", ( entryId, ))

