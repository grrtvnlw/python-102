# get temperature from user in Celsius
temp_C = float(input('Temperature in C? '))

#convert Celsius to Fahrenheit
temp_F = temp_C * (9 / 5) + 32

#display temperature in Fahrenheit
print(f'{temp_F} F')