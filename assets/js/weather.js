
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

  if (!response1.ok){

    document.getElementById("weather-data").innerHTML = "Q: How does a hurricane see?<br>A: With its eye."

  } else if (response1.ok){

    const data1 = await response1.json(); 

    const response2 = await fetch(data1.properties.forecast); 

    if (!response2.ok) {

      document.getElementById("weather-data").innerHTML = "Q: How does a hurricane see?<br>A: With its eye."

    } else if (response2.ok) {

      const data2 = await response2.json()

      document.getElementById("weather-data").innerHTML = data2.properties.periods[0].detailedForecast

    }

  }
  
} 

// Calling the function every hour
setInterval(getWeather(), 1000 * 60 * 60 * 1);


