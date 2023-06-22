class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        kelvin = round(celsius + 273.15, 5)
        fahrenheit = round(celsius * 1.8 + 32, 5)
        return [kelvin, fahrenheit]