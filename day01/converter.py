temperature_celsius = float(input("Enter temperature in Celsius: "))
distance_km = float(input("Enter distance in kilometers: "))

temperature_fahrenheit = (temperature_celsius * 9/5) + 32
distance_miles = distance_km * 0.621371

print(f"Temperature in Fahrenheit: {temperature_fahrenheit:.2f}°F")
print(f"Distance in Miles: {distance_miles:.2f} miles")
