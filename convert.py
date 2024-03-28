def convert_to_celsius(fahrenheit):

 '''(number) -> number

    Return the number of Celsius degrees equivalent to fahrenheit degrees.

    >>>convert_to_celsius(32)
    0
    >>>convert_to_celsius(212)
    100
 '''
 return(fahrenheit - 32) * 5 / 9 
    
fahrenheit = input("Enter the temperature in Fahrenheit to be converted to Celsius: ")

celsius = convert_to_celsius(fahrenheit)

print(celsius)


