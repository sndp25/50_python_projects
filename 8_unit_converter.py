# Distance Conversion Function
def distance_conv(val, unitin, unitout):
    # Convert the input value to millimeters
    if unitin == "mm":
        value_in_mm = val
    elif unitin == "cm":
        value_in_mm = val * 10
    elif unitin == "m":
        value_in_mm = val * 1000
    elif unitin == "km":
        value_in_mm = val * 1000000
    else:
        return "Invalid distance unit"

    # Convert millimeters to the desired output unit
    if unitout == "mm":
        return value_in_mm
    elif unitout == "cm":
        return value_in_mm / 10
    elif unitout == "m":
        return value_in_mm / 1000
    elif unitout == "km":
        return value_in_mm / 1000000
    else:
        return "Invalid distance unit"


# Time Conversion Function
def time_conv(val, unitin, unitout):
    # Convert the input value to seconds
    if unitin == "seconds":
        value_in_seconds = val
    elif unitin == "minutes":
        value_in_seconds = val * 60
    elif unitin == "hours":
        value_in_seconds = val * 3600
    elif unitin == "days":
        value_in_seconds = val * 86400
    else:
        return "Invalid time unit"
    
    # Convert seconds to the desired output unit
    if unitout == "seconds":
        return value_in_seconds
    elif unitout == "minutes":
        return value_in_seconds / 60
    elif unitout == "hours":
        return value_in_seconds / 3600
    elif unitout == "days":
        return value_in_seconds / 86400
    else:
        return "Invalid time unit"


# Mass Conversion Function
def mass_conv(val, unitin, unitout):
    # Convert the input value to grams
    if unitin == "grams":
        value_in_grams = val
    elif unitin == "kilograms":
        value_in_grams = val * 1000
    elif unitin == "tons":
        value_in_grams = val * 1000000
    else:
        return "Invalid mass unit"

    # Convert grams to the desired output unit
    if unitout == "grams":
        return value_in_grams
    elif unitout == "kilograms":
        return value_in_grams / 1000
    elif unitout == "tons":
        return value_in_grams / 1000000
    else:
        return "Invalid mass unit"

# Testing the functions

# Distance Conversion
print("Distance Conversion:")
print(distance_conv(10, "mm", "cm"))  # 10 mm to cm
print(distance_conv(10, "cm", "m"))   # 10 cm to meters
print(distance_conv(1, "km", "mm"))   # 1 km to mm

# Time Conversion
print("\nTime Conversion:")
print(time_conv(5, "minutes", "seconds"))  # 5 minutes to seconds
print(time_conv(2, "hours", "minutes"))    # 2 hours to minutes
print(time_conv(3, "days", "hours"))       # 3 days to hours

# Mass Conversion
print("\nMass Conversion:")
print(mass_conv(500, "grams", "kilograms"))  # 500 grams to kilograms
print(mass_conv(2, "tons", "grams"))        # 2 tons to grams
