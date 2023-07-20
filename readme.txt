
# JSON to SQLite Converter

This is a simple web application that allows you to convert JSON data into an SQLite database file (.db). The application is built by Adham using Flask (Python web framework) and provides a basic user interface to paste the JSON data and download the converted SQLite database.

## Prerequisites

Make sure you have the following installed on your system:

- Python (version 3.6 or higher)
- Flask (Python web framework)
- pandas library

## Getting Started

1. Clone the repository to your local machine:

```
https://github.com/demo55oo/upworkpythonscript/

```

2. Install the required libraries:

```
pip install flask pandas
```

## How to Use

1. Run the Flask web application:

```
python app.py
```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. You will see a web page titled "JSON to SQLite Converter."

4. Paste your JSON data into the textarea provided.

5. Click the "Convert to SQLite" button.

6. The application will convert the JSON data into an SQLite database and prompt you to download the `sqlite.db` file.

## Note

- The application assumes that the JSON data provided is an array of objects, where each object represents a row in the SQLite database table. The keys of the objects will be used as column names in the table.

- If there are any errors during the conversion process, the application will display an error message.
