#
#
#
#
animals = {

"Lion" : "Cub",
"Cat" : "Kitten",
"Dog" : "puppy",
"Sheep" : "Lamb",
"Gecko" : "baby Gecko"
}

input_animal = input("Enter an animal name   ")
input_baby = input("Enter a baby name   ")

Existsflag = False

for i in animals:
    if i == input_animal:
        Existsflag=True
        print(animals.get(i))

if Existsflag == False:
    animals.update({input_animal : input_baby})

print(animals)
