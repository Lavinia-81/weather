#### Weather Application

This application provides weather information for a given city, including temperature, pressure, and wind speed. It uses a GUI built with Gradio.

## Features
- Fetch temperature, pressure, and wind speed for a specified city.
- Interactive buttons for user-friendly experience.
- Display results in a GUI textbox.
- Configurable settings for cities, weather API, and notification systems.

## Installation
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Configuration
- Make sure to update the config.json file with your weather API settings.

## Usage
- Run the application:
```python weather_forecast.py```

- Enter the city name in the textbox.
- Click on the desired button (Temperature, Pressure, Wind Speed) to get the corresponding weather information.

## Files
- weather_forecast.py: The main script that initializes the GUI and handles user interactions.
- config.json: Configuration file for weather API settings.
- requirements.txt: A list of required Python packages.
- weather_forecast.py: Python module for fetching weather information.

## Example
- Here is an example of how to use the application:
```
City: London
Result: Temp: 15°C
```

## Acknowledgements
- This application uses Gradio for the GUI and a weather API for fetching weather data.
- Feel free to customize this `README.md` to match your specific application details. If you need further assistance, let me know!
