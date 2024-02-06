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

### to test if we have completed loop and not found the animal in the list
Existsflag = False

### loop through keys of dictionary, i will represent key

for i in animals:
    if i == input_animal:
        Existsflag=True
        print(animals.get(i))


### this is out of the if and the loop, so if flag is false we have not found animal
### we can the add the animal as per instructions        

if Existsflag == False:
    animals.update({input_animal : input_baby})

print(animals)
