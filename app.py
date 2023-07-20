import pandas as pd
import sqlite3
from flask import Flask, request, jsonify, send_file
from pandas import json_normalize

app = Flask(__name__)

def convert_json_to_sqlite(json_data):
    # Flatten the nested JSON data
    flattened_data = json_normalize(json_data)

    # Convert data types to string (to handle various data types in JSON)
    flattened_data = flattened_data.astype(str)

    # Implement your JSON to SQLite conversion logic here
    # Create an in-memory SQLite database
    conn = sqlite3.connect(":memory:")

    # Write the flattened data to SQLite
    flattened_data.to_sql('data_table', conn, index=False)

    # Create the target SQLite database file
    target_file = "sqlite.db"
    target_conn = sqlite3.connect(target_file)

    # Copy the data from the in-memory database to the target file
    conn.backup(target_conn)

    # Close the connections
    conn.close()
    target_conn.close()

    # Return the SQLite database file path
    return target_file

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return send_file('index.html')
    elif request.method == 'POST':
        try:
            json_data = request.get_json()
            if not json_data:
                return jsonify({'message': "Paste your JSON data and click 'Convert to SQLite'."}), 400

            sqlite_file = convert_json_to_sqlite(json_data)
            return send_file(sqlite_file, as_attachment=True)

        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
