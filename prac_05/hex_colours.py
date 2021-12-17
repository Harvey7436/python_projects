COLOR_NAME = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "#f0f8ff",
                "Alizarincrimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}
print(COLOR_NAME)

color_code = input("Enter color: ")
while color_code != "":
    if color_code in COLOR_NAME:
        print(color_code, "is", COLOR_NAME[color_code])
    else:
        print("Invalid color")
    color_code = input("Enter color: ")
