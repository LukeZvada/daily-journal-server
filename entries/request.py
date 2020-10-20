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
















# Hey team! I will be handling the data collection to update our class JSON file. All I really need from you is to use the following template. Don't worry about the Img fields, and if you don't have the personal site complete leave that blank as well.
# Respond to this thread with the data, and I will take it from there. Deadline to get this info to me (except the portfolio site which can be left blank for now) will be 27 October. Please complete this whenever you get a moment, thanks!
# {
#             "id": 9,
#             "firstName": "Luke",
#             "lastName": "Zvada",
#             "reelThemIn": "An easy solution",
#             "bio": "Previously working in the music industry as a tour manager, I learned how to solve issues on the go, organize a complicated schedule, and manage team morale. Through that hard work, I have found a new passion for software development. I attended Nashville Software School that allowed me to take that new passion and turn it into reality. Having strong attributes such as problem solving, dependability, and efficiency, I have embraced this new opportunity in tech and continue to learn and grow as a software developer every day. ",
#             "github": "https://github.com/LukeZvada",
#             "linkedIn": "https://www.linkedin.com/in/lukezvada/",
#             "portfolio": "",
#             "email": "luke.zvada@gmail.com",
#             "proImg": "",
#             "funImg": ""
#         }