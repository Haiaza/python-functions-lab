# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.
def calculate_area_triangle(base, height):
    return (base * height) / 2


print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


print('Exercise 2:', simple_interest(1000, 5, 2))

# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.


def apply_discount(price, discount):
    discount_value = price * (discount/100)
    return (price - discount_value)


print('Exercise 3:', apply_discount(100, 25))

# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.
def convert_temperature(temp, unit):
    # the accepted units
    accepted_units = ["C", "F"]
    # loop asking the user for their input of temp and unit
    while True:
        # temp must be a number
        try:
            temp = float(input("Please input a temperature "))
            
            unit = input("Please input a temperature unit ").upper()

            # check whether the users unit is inside the accpepted units list
            if unit not in accepted_units:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue        # restart the loop now that instruction has been given

            # if both temp and unit pass, break out of the while loop
            break

        except ValueError:
            print("This isnt a good value, try something numeric.")

    # Convert temperature based on unit
    if unit == "C":
        converted = (temp * 9/5) + 32  # Convert to Fahrenheit
        print(f"{temp}°C is {converted}°F.")
    elif unit == "F":
        converted = (temp - 32) * 5/9  # Convert to Celsius
        print(f"{temp}°F is {converted}°C.")





print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))
