#TempConvert.py
#Name:Edip Uman
#Date:2/8/2026
#Assignment:Lab 03


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = float(input("What is the current temperature in your area in Fahrenheit?"))
  tempC = round((tempF - 32) * (5/9), 1)

  print(tempF, "is", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
