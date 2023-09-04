celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

fahrenheit = int(fahrenheit * 100) / 100.0

print('%.2f Celsius is equivalent to: %.2f Fahrenheit'
      % (celsius, fahrenheit))