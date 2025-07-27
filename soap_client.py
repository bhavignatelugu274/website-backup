from zeep import Client

wsdl = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"
client = Client(wsdl=wsdl)

# Convert Celsius to Fahrenheit
result = client.service.CelsiusToFahrenheit('100')
print("100°C =", result)



