# get temperature from user in Celsius
tempC = float(input('Temperature in C? '))

#convert Celsius to Fahrenheit
tempF = tempC * (9 / 5) + 32

#display temperature in Fahrenheit
print(f'{tempF} F')