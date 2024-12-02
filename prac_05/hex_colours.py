"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

COLOUR_TO_HEX = {"amethyst": "#9966cc", "blueviolet": "#8a2be2", "byzantine": "#bd33a4", "byzantium": "#702963",
                 "dark byzantium": "#5d3954", "dark lavender": "#734f96", "darkorchid": "#9932cc",
                 "darkorchid1": "#bf3eff", "darkorchid2": "#b23aee", "darkorchid3": "#9a32cd", "DarkOrchid4": "#68228b"}
print(COLOUR_TO_HEX)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
