const https = require('https');
const readline = require('readline');

const API_KEY = '939685597c5488b0301576376e2c6836'; // Replace with your OpenWeatherMap API key

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function fetchWeather(city) {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`;

    https.get(url, (resp) => {
        let data = '';

        // A chunk of data has been received.
        resp.on('data', (chunk) => {
            data += chunk;
        });

        // The whole response has been received.
        resp.on('end', () => {
            const weather = JSON.parse(data);
            if (weather.cod === 200) {
                console.log(`Weather in ${weather.name}, ${weather.sys.country}:`);
                console.log(`Temperature: ${weather.main.temp}°C`);
                console.log(`Weather: ${weather.weather[0].description}`);
                console.log(`Humidity: ${weather.main.humidity}%`);
                console.log(`Wind Speed: ${weather.wind.speed} m/s`);
            } else {
                console.log(`Error: ${weather.message}`);
            }
            rl.close();
        });

    }).on("error", (err) => {
        console.log("Error: " + err.message);
        rl.close();
    });
}

rl.question('Enter a city name to get the weather: ', (city) => {
    fetchWeather(city);
});