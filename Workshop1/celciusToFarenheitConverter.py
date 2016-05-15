print('Temperature Conversion Program')
print()

celciusValue = float(input('Please enter the temperature in Celcius to convert to Farenheit and Kelvin: '))
print()

farenheitValue = celciusValue * 9 / 5 + 32
kelvinValue = celciusValue + 273.15

print('The original temperature in Celcius was\n\t\t', celciusValue)
print()
print('The temperature converted to Farenheit is\n\t\t', farenheitValue)
print()
print('The temperature converted to Kelvin is\n\t\t', kelvinValue)