
// National Weather Service API
const api_url = "https://api.weather.gov/points/"; 

// Latitude and Longitude of Cambridge, MA According to https://nominatim.openstreetmap.org/ui/search.html 
const Latitude = 42.3655; 
const Longitude = -71.1040; 

const date = new Date();
const hour = date.getHours();
const min = date.getMinutes();

async function getWeather() { 

  // Making an API call (request) 
  // and getting the response back 
  const response1 = await fetch((api_url + Latitude + "," + Longitude)); 
  
  // Parsing it to JSON format 
  const data1 = await response1.json(); 

  const response2 = await fetch(data1.properties.forecast); 

  const data2 = await response2.json()

  document.getElementById("weather-data").innerHTML = data2.properties.periods[0].detailedForecast
    
} 

// Calling the function every 2 hours
setInterval(getWeather(), 1000 * 60 * 60 * 2);


