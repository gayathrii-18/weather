# Real-Time Weather Monitoring System

This project implements a real-time data processing system for weather monitoring, utilizing the OpenWeatherMap API to retrieve and analyze weather data for major Indian cities.

## Features

- Retrieves weather data for Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad
- Processes and stores weather data in a SQLite database
- Calculates daily weather summaries
- Implements an alerting system for user-defined weather thresholds
- Provides a web interface for visualizing weather data and summaries

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/weather-monitoring-system.git
   cd weather-monitoring-system
   ```

2. Create a `.env` file in the root directory with the following content:
   ```
   OPENWEATHERMAP_API_KEY=your_api_key_here
   SMTP_SERVER=your_smtp_server
   SMTP_PORT=your_smtp_port
   SMTP_USERNAME=your_email@example.com
   SMTP_PASSWORD=your_email_password
   ```

3. Build and run the Docker container:
   ```
   docker-compose up --build
   ```

4. Access the application at `http://localhost:5000`

## Running Tests

To run the test suite:
