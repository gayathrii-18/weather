import React from 'react';

function WeatherDisplay({ data }) {
  return (
    <div className="weather-display">
      <h2>Current Weather</h2>
      {Object.entries(data).map(([city, cityData]) => (
        <div key={city} className="city-weather">
          <h3>{city}</h3>
          <p>Temperature: {cityData.temp}°C</p>
          <p>Feels Like: {cityData.feels_like}°C</p>
          <p>Condition: {cityData.main}</p>
        </div>
      ))}
    </div>
  );
}

export default WeatherDisplay;
