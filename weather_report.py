import requests


def get_weather_data(date):
    base_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        weather_data = []
        for item in data['list']:
            if item['dt_txt'].startswith(date):
                weather_data.append(item)
        return weather_data if weather_data else f"No weather data available for {date}"
    else:
        return f"Error fetching weather data. Status Code: {response.status_code}"

if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            selected_date = input("Enter the date (YYYY-MM-DD): ")
            weather_data = get_weather_data(selected_date)
            if isinstance(weather_data, list):
                for item in weather_data:
                    temperature_kelvin = item['main']['temp']
                    print(f"Date: {item['dt_txt']}, Temperature: {temperature_kelvin} Kelvin")
            else:
                print(weather_data)
        elif choice == '2':
            selected_date = input("Enter the date (YYYY-MM-DD): ")
            weather_data = get_weather_data(selected_date)
            if isinstance(weather_data, list):
                for item in weather_data:
                    wind_speed = item['wind']['speed']
                    print(f"Date: {item['dt_txt']}, Wind Speed: {wind_speed} m/s")
            else:
                print(weather_data)
        elif choice == '3':
            selected_date = input("Enter the date (YYYY-MM-DD): ")
            weather_data = get_weather_data(selected_date)
            if isinstance(weather_data, list):
                for item in weather_data:
                    pressure = item['main']['pressure']
                    print(f"Date: {item['dt_txt']}, Pressure: {pressure} hPa")
            else:
                print(weather_data)
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
