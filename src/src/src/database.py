import sqlite3

DB_NAME = 'weather.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather_data
                 (city TEXT, main TEXT, temp REAL, feels_like REAL, dt INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS daily_summaries
                 (date TEXT, city TEXT, avg_temp REAL, max_temp REAL, min_temp REAL, dominant_condition TEXT)''')
    conn.commit()
    conn.close()

def insert_weather_data(processed_data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    for city, data in processed_data.items():
        c.execute('INSERT INTO weather_data VALUES (?, ?, ?, ?, ?)',
                  (city, data['main'], data['temp'], data['feels_like'], data['dt']))
    conn.commit()
    conn.close()

def insert_daily_summary(date, city, summary):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO daily_summaries VALUES (?, ?, ?, ?, ?, ?)',
              (date, city, summary['avg_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    conn.commit()
    conn.close()
