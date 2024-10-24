from collections import Counter

def process_weather_data(weather_data):
    processed_data = {}
    for city, data in weather_data.items():
        processed_data[city] = {
            'main': data['weather'][0]['main'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'dt': data['dt']
        }
    return processed_data

def calculate_daily_summary(data):
    temps = [d['temp'] for d in data]
    weather_conditions = [d['main'] for d in data]
    return {
        'avg_temp': sum(temps) / len(temps),
        'max_temp': max(temps),
        'min_temp': min(temps),
        'dominant_condition': Counter(weather_conditions).most_common(1)[0][0]
    }
