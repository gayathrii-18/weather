import React, { useState, useEffect } from 'react';
import WeatherDisplay from './components/WeatherDisplay';
import DailySummary from './components/DailySummary';
import AlertsDisplay from './components/AlertsDisplay';
import './App.css';

function App() {
  const [weatherData, setWeatherData] = useState({});
  const [dailySummary, setDailySummary] = useState({});
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    // Fetch data from your backend API
    const fetchData = async () => {
      const response = await fetch('http://localhost:5000/api/weather');
      const data = await response.json();
      setWeatherData(data);
    };

    fetchData();
    // Set up interval to fetch data every 5 minutes
    const interval = setInterval(fetchData, 300000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <h1>Weather Monitoring System</h1>
      <WeatherDisplay data={weatherData} />
      <DailySummary data={dailySummary} />
      <AlertsDisplay alerts={alerts} />
    </div>
  );
}

export default App;
