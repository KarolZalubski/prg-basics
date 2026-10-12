###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
# Wprowadzenie temperatury w stopniach C
celcius = int(input("Wprowadź temperaturę w stopniach Celcjusza: "))
# Zamiana na Farenheity oraz Kelviny
farenheit = celcius*1.8 + 32
kelvin = celcius + 273.15
# wypisanie temperatur
print(f"Farenheit: {farenheit}")
print(f"Kelvin: {kelvin}")