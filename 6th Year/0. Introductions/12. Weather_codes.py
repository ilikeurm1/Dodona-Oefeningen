def get_weather_code():
    rain = bool(int(input("Is it raining? (1/0): ")))
    if not rain:
        return "green"

    wind_speed = int(input("Enter wind speed (in km/h): "))
    if wind_speed <= 100:
        return "yellow"
    elif wind_speed <= 130:
        return "orange"
    else:
        return "red"
    
print(f"The weather code is: {get_weather_code()}")
