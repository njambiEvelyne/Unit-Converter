#From kilograms to pounds
kilogram_pound = 5/9
pound_kilogram = 9/5

"""Getting the user weight in KG"""
try: 
  weight_entry_unit = input("Is your weight in kg's or in pound:  ").lower()
  if weight_entry_unit == "kg":
    weight = int(input("Enter your weight: "))
    converted_weight = weight * kilogram_pound
    print(f"You are {converted_weight} pounds")
  
  elif weight_entry_unit == "pound":
    weight = int(input("Enter your weight in pounds: "))
    converted_weight = weight * pound_kilogram
    print(f"You are {converted_weight} kilograms.")

  else:
    print("Invalid Convertion Unit!")


except ValueError:
  print("Invalid Input!")