#
#
#
#
animals =  {'Lion': 'Cub', 'Cat': 'Kitten', 'Dog': 'puppy', 'Sheep': 'Lamb', 'Gecko': 'Hatchling',
             'Zebra': 'Foal', 'Fish': 'Fry', 'Crab': 'Zoea'}

user_input = input("please enter an animal name   ")

ExistsFlag = False

for i in animals:
    if i == user_input:
        print(animals.get(i))
        ExistsFlag = True
    
if ExistsFlag == False:
    print("animal not in list")
