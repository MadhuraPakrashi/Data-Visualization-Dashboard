import json
import csv

json_file = "C:\\Users\\user\\Desktop\\Blackcoffer\\jsondata.json"
csv_file = "C:\\Users\\user\\Desktop\\Blackcoffer\\data.csv"

with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

field_names = data[0].keys()

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    csv_writer = csv.DictWriter(f, fieldnames=field_names)
    csv_writer.writeheader()
    csv_writer.writerows(data)

from flask import Flask, render_template, jsonify, request
import mysql.connector
import os
app = Flask(__name__)


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'pakrashimadhura@23',
    'database': 'blackcoffer_data'
}

LIBRARY_DIR = os.path.join(app.root_path, 'static', 'libraries')

@app.route('/', methods=['GET'])
def index():
    return render_template('dashboard.html')


@app.route('/get_data', methods=['GET'])
def get_data():
    try:

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)


        selected_end_year = request.args.get('endYear')
        selected_topic = request.args.get('topic')


        query = "SELECT * FROM articles WHERE 1=1"
        if selected_end_year:
            query += f" AND end_year = '{selected_end_year}'"
        if selected_topic:
            query += f" AND topic = '{selected_topic}'"


        cursor.execute(query)
        data = cursor.fetchall()

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()
        conn.close()



@app.route('/get_end_years', methods=['GET'])
def get_end_years():
    try:

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()


        query = "SELECT DISTINCT end_year FROM articles"
        cursor.execute(query)
        end_years = [str(row[0]) for row in cursor.fetchall()]

        return jsonify(end_years)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()
        conn.close()

@app.route('/get_topics', methods=['GET'])
def get_topics():
    try:

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()


        query = "SELECT DISTINCT topic FROM articles"
        cursor.execute(query)
        topics = [row[0] for row in cursor.fetchall()]

        return jsonify(topics)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()
        conn.close()




if __name__ == '__main__':
    app.run(debug=True)
