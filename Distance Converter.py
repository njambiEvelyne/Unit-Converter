"""
This module will be used to convert distance from miles to km and vise versa
"""
MILES_TO_KM = 1.60934
KM_TO_MILES = 0.621371

"""
This method converts the distance from km to miles
"""
def km_to_miles_converter():
  distance = float(input("Enter the distance in km: "))
  result = distance * KM_TO_MILES
  return f"{distance} km is equal to {result:.2f} miles."

"""
This method converts the distance from miles to km
"""
def miles_to_km_converter():
  distance = float(input("Enter the distance in miles"))
  result = distance * MILES_TO_KM
  return f"{distance} miles is equal to {result:.2f} km"

"""
This method will be used for user entry convertions
"""
def converter():
  distance_unit = input("Is the distance in km or in miles: ")
  if distance_unit == "km":
    print(km_to_miles_converter())
  
  elif distance_unit == "miles":
    print(miles_to_km_converter)

  else:
    print("Invalid Input! Please enter 'km' or 'miles'.")
  
converter ()

