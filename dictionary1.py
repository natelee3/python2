meal = {
    "entree": "smash burgers",
    "drink": "IPA",
    "side": "fries",
    "dessert": "oreos"
}


# if "dessert" in meal:
#     print("Of course I had dessert!")
# else:
#     print("I didn't have dessert")

meal["appetizer"] = "bloomin' Onion"
meal["drink"] = "sweet tea"
del meal["side"]

for key, value in meal.items():
    print("My %s tonight was %s" % (key, value))

