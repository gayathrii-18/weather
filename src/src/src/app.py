from flask import Flask, render_template, jsonify
from weather_fetcher import fetch_weather_data
from data_processor import process_weather_data, calculate_daily_summary
from database import insert_weather_data, insert_daily_summary
from alert_system import check_thresholds, send_alert
import schedule
import time
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather')
def get_weather():
    weather_data = fetch_weather_data()
    processed_data = process_weather_data(weather_data)
    return jsonify(processed_data)

def update_weather():
    weather_data = fetch_weather_data()
    processed_data = process_weather_data(weather_data)
    insert_weather_data(processed_data)
    
    # Calculate and store daily summary
    for city, data in processed_data.items():
        summary = calculate_daily_summary([data])
        insert_daily_summary(time.strftime('%Y-%m-%d'), city, summary)
    
    # Check for alerts
    alerts = check_thresholds(processed_data, {'high_temp': 35, 'low_temp': 10})
    for alert in alerts:
        send_alert("Weather Alert", alert, "your_email@example.com")

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    schedule.every(5).minutes.do(update_weather)
    threading.Thread(target=run_schedule).start()
    app.run(debug=True)
