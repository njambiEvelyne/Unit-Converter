# CELSIUS_TO_FAHRENHEIT = -17.22
# FAHRENHEIT_TO_CELSIUS = 33.8
import emoji


def cels_to_fahr():
  temp = float(input("Enter the degree celsius: "))
  temperature = (temp * 9/5) + 32 
  print(f"{temp} degress celsius is equal to {temperature:.2f} Fahreinheit")

def fahr_to_cels():
  temp =float(input("Enter the temperature in fahrenheit: "))
  temperature = (temp - 32) * 5/9  # Corrected formula
  print(f"{temp} Fahrenheit is equal to {temperature:.2f} Degress Celsius.")


def converter():
    """Handles user input and calls the appropriate conversion function."""
    temp_unit = input("Is the temperature in 'celsius' or 'fahrenheit'? ").strip().lower()

    if temp_unit == "celsius":
        cels_to_fahr()
        print(emoji.emojize("Temperature converted successfully! 😊"))

    elif temp_unit == "fahrenheit":
        fahr_to_cels()
        print(emoji.emojize("Temperature converted successfully! 😊"))

    else:
        print(emoji.emojize("Invalid input! Please enter 'celsius' or 'fahrenheit'. 😢"))

# Run the converter
converter()

