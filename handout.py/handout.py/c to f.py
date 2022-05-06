def celsius_para_fahrenheit(temperatura_celsius):
    temperatura_fahrenheit= (1.8*temperatura_celsius)+32
    return temperatura_fahrenheit
temperatura_celsius=int(input('qual o valor de celsius?'))
print(celsius_para_fahrenheit(temperatura_celsius))
