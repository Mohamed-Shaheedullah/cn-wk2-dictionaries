### This is the work done on python dictionaries

# git add .
# git commit -m "A SIMPLE MESSAGE"
# git push
##

capital_cities = {
"England" : "London",
"Scotland" : "Edinburgh",
"Wales" : "Cardiff",
"Northern Ireland" : " Belfast",
"Ireland" : "Dublin"
}


four_animals = {

"Lion" : "Cub",
"Cat" : "Kitten",
"Dog" : "puppy",
"Sheep" : "Lamb",
"Gecko" : "baby Gecko"
}

print(four_animals)

print(four_animals["Dog"])

four_animals["Gecko"] = "Hatchling"

print(four_animals)

print(four_animals.keys())

print(four_animals.values())

print(four_animals.items())

### tghe get method returns the value of a key

print(four_animals.get("Gecko"))

print(four_animals.get("TRex", "not exist"))

print(four_animals.setdefault("Zebra", "Foal"))

print(four_animals.update({"Fish" : "Fry", "Crab": "Zoea"}))
      
print(four_animals)

four_animals.popitem()

print(four_animals)





