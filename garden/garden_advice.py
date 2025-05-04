"""Issue one: remove hardcoded variable values
- Replaced season = "summer" variable and added user input
- Replaced plant_type = "flower" variable and added user input"""
season = input("Choose a season: winter or summer: ").lower()
plant_type = input("Choose either flower or vegetable: ").lower()

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

"""Issue two: add plant recommendations based on
season and plant type choices"""
# Determine plant recommendation based on the season and plant type
if plant_type == "flower" and season == "summer":
    advice += "Summer flower recommendations: Sunflower, Azaleas,"
    " and Peace Lillies"
elif plant_type == "flower" and season == "winter":
    advice += "Winter flower recommendations: Snapdragons,"
    " Hyacinth, and Witch Hazel"
elif plant_type == "vegetable" and season == "summer":
    advice += "Summer vegetable recommendations: Corn, Green Beans, Tomatoes"
elif plant_type == "vegetable" and season == "winter":
    advice += "Winter vegetable recommendations: Acorn Squash,"
    " Sweet Potatoes, Turnips"

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
