import sys

message = f"""

Usage: python3 {sys.argv[0]} [Color 1] [Color 2] ... [Multiplier]

if your resistor is 4 band type, then write:
    python3 {sys.argv[0]} [Color 1] [Color 2] [Multiplier]

but if your resistor is 5 band type, then write:
    python3 {sys.argv[0]} [Color 1] [Color 2] [Color 3] [Multiplier]

"""

color = {
        "Black": 0,
        "Brown": 1,
        "Red": 2,
        "Orange": 3,
        "Yellow": 4,
        "Green": 5,
        "Blue": 6,
        "Purple": 7,
        "Gray": 8,
        "White": 9
}

multiplier = {
        "Black": (10**0),
        "Brown": (10**1),
        "Red": (10**2),
        "Orange": (10**3),
        "Yellow": (10**4),
        "Green": (10**5),
        "Blue": (10**6),
        "Purple": (10**7),
        "Gray": (10**8),
        "White": (10**9),
        "Gold": (10**-1),
        "Silver": (10**-2)
}

tolerance = {
        "Brown": 1,
        "Red": 2,
        "Green": 0.5,
        "Blue": 0.25,
        "Purple": 0.1,
        "Gray": 0.05,
        "Gold": 5,
        "Silver": 10
}

if len(sys.argv) != 4 and len(sys.argv) != 5:
    print(message)

else:
    if (len(sys.argv)-1) == 4:
        color_1 = sys.argv[1]
        color_2 = sys.argv[2]
        multiply_input = sys.argv[3]
        tolerance_input = sys.argv[4]
    
        color_1 = color_1.title()
        color_2 = color_2.title()
        multiply_input = multiply_input.title()
        tolerance_input = tolerance_input.title()

        if color_1 in color:
            color_value1 = color[color_1]
        else:
            color_value1 = "Unknown"
    

        if color_2 in color:
            color_value2 = color[color_2]
        else:
            color_value2 = "Unknown"


        if multiply_input in multiplier:
            multiply_value = multiplier[multiply_input]
        else:
            multiply_value = "Unknown"
        
        if tolerance_input in tolerance:
            tolerance_value = tolerance[tolerance_input]
        else:
            tolerance_value = "Unknown"
        

        if color_value1 != "Unknown" and color_value2 != "Unknown" and multiply_value != "Unknown" and tolerance_input != "Unknown":
            gabung = int(str(color_value1) + str(color_value2))
            hasil = gabung * multiply_value
            
            if str(hasil)[3:] == "000":
                print("Result: %s ohm" % str(hasil // 1000))
                print(f"Tolerance: {tolerance_value}% ({tolerance_input})")
            elif str(hasil)[3:] == "000000":
                print("Result: %s ohm" % str(hasil // 1000000))
                print(f"Tolerance: {tolerance_value}% ({tolerance_input})") 
            elif str(hasil)[3:] == "000000000":
                print("Result: %s ohm" % str(hasil // 1000000000))
                print(f"Tolerance: {tolerance_value}% ({tolerance_input})")
            else:
                print("Result: %d ohm" % (hasil))
                print(f"Tolerance: {tolerance_value}% ({tolerance_input})")
        else:
            print("The color is not on the list")


    elif (len(sys.argv)-1) == 5:
        color_1 = sys.argv[1]
        color_2 = sys.argv[2]
        color_3 = sys.argv[3]
        multiply_input = sys.argv[4]
        tolerance_input = sys.argv[5]
    
        color_1 = color_1.title()
        color_2 = color_2.title()
        color_3 = color_3.title()
        multiply_input = multiply_input.title()
        tolerance_input = tolerance_input.title()

        if color_1 in color:
            color_value1 = color[color_1]
        else:
            color_value1 = "Unknown"
    

        if color_2 in color:
            color_value2 = color[color_2]
        else:
            color_value2 = "Unknown"

    
        if color_3 in color:
            color_value3 = color[color_3]
        else:
            color_value3 = "Unknown"


        if multiply_input in multiplier:
            multiply_value = multiplier[multiply_input]
        else:
            multiply_value = "Unknown"

        
        if tolerance_input in tolerance:
            tolerance_value = tolerance[tolerance_input]
        else:
            tolerance_value = "Unknown"

        if color_value1 != "Unknown" and color_value2 != "Unknown" and color_value3 != "Unknown" and multiply_value != "Unknown" and tolerance_value != "Unknown":
            gabung = int(str(color_value1) + str(color_value2) + str(color_value3))
            hasil = gabung * multiply_value


            if str(hasil)[3:] == "000":
                print("Result: %s ohm" % str(hasil // 1000))
                print(f"Tolerance: {tolerance_value}% ({tolerance_input})")
            elif str(hasil)[3:] == "000000":
                print("Result: %s ohm" % str(hasil // 1000000))
                print(f"Tolerance: {tolerance_value}% ({tolerance_input})") 
            elif str(hasil)[3:] == "000000000":
                print("Result: %s ohm" % str(hasil // 1000000000))
                print(f"Tolerance: {tolerance_value}% ({tolerance_input})")
            else:
                print("Result: %d ohm" % (hasil))
                print(f"Tolerance: {tolerance_value}% ({tolerance_input})")
        else:
            print("The color is not on the list")

