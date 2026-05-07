import requests


def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        wind_speed = current["windspeedKmph"]
        condition = current["weatherDesc"][0]["value"]

        print("\nWeather Report")
        print(f"City: {city}")
        print(f"Condition: {condition}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")

    except requests.exceptions.RequestException:
        print("Could not connect to the weather service.")
    except KeyError:
        print("Weather data was not found for this city.")


def main():
    print("--- Weather App ---")

    while True:
        city = input("\nEnter city name or type exit: ")

        if city.lower() == "exit":
            print("Program closed.")
            break

        if city.strip() == "":
            print("City name cannot be empty.")
        else:
            get_weather(city)


if __name__ == "__main__":
    main()