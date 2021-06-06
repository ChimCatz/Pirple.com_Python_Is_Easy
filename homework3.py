# HOMEWORK #3 If Statements

# Change to "Hot" or "Cold" for Weather
Weather = "Cold"
# Change Temperature value to any Integer or String
Temperature = "9"

Temperature = int(Temperature)

Umbrella = True
Jacket = False

# IF statement conditions and output
if Weather == "Hot" and Temperature >= 25:
    Umbrella = True
    Jacket = False
    print("The weather is hot, please bring your umbrella")

elif Weather == "Cold" and Temperature <= 15:
    Umbrella = False
    Jacket = True
    print("The weather is cold, please wear your jacket")
else:
    print("The weather is lovely, enjoy your day")
    Umbrella = False
    Jacket = False

print(Umbrella)
print(Jacket)
