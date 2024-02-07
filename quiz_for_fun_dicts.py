#
### M R Shaheedullah
#
### Quiz Game
#
import colorama
from colorama import Fore
colorama.init(autoreset=True)


q_and_a = {"Who was the first man on the moon?": 
           [
            "A:  Neil armstrong", 
            " B: Buzz aldren",
             "C: Albert Einstine", 
             "D: Liam clayton"
             ] ,
             "What is the largest planet in our solar system?" :
               ["A: Mars", 
             "B: Jupiter", 
             "C: Earth", 
             "D:Saturn"
             ],
            "Whats the tallest building?":
             [
                 "A: Ping An Finance Centre - Shenzhen, China", 
             "B: Shanghai Tower - Shanghai, China", 
             "C: Burj Khalifa - Dubai, United Arab Emirates",
             "D: Abraj Al-Bait Clock Tower - Mecca, Saudi Arabia"
             ],
              "What is the capital Turkey?" :
                  [
                      "A: Istanbul", 
             "B: Ankara", 
             "C: Bursa", 
             "D: Konya"
             ],
             "What is the speed of light?" :
            [
                   "A: 300,000,000 mph", 
             "B: 300,000,000 m/s",
             "C: 300,000,000 kph", 
             "D: 300,000,000 cm/s"
             ]
         
             }



### set initial score

score = 0

### function for checking answer

def check_ans(q_number, users_answer):
    global q_num
    q_num += 1
    global score
    print(q_number, users_answer)
    if q_number == 0 and users_answer == "A":
        print(Fore.GREEN + "Correct!")
        score += 5
    elif q_number == 0 and users_answer != "A":
        print(Fore.RED + "Incorrect. The correct answer is: A ")
        score -= 2
    if q_number == 1 and users_answer == "B":
        print(Fore.GREEN + "Correct!")
        score += 5
    elif q_number == 1 and users_answer != "B":
        print(Fore.RED + "Incorrect. The correct answer is: B ")
        score -= 2
    if q_number == 2 and users_answer == "C":
        print(Fore.GREEN + "Correct!")
        score += 5
    elif q_number == 2 and users_answer != "C":
        print(Fore.RED + "Incorrect. The correct answer is: C")
        score -= 2
    if q_number == 3 and users_answer == "B":
        print(Fore.GREEN + "Correct!")
        score += 5
    elif q_number == 3 and users_answer != "B":
        print(Fore.RED + "Incorrect. The correct answer is: B ")
        score -= 2
    if q_number == 4 and users_answer == "C":
        print(Fore.GREEN + "Correct!")
        score += 5
    elif q_number == 4 and users_answer != "C":
        print(Fore.RED + "Incorrect. The correct answer is: C ")
        score -= 2
    print(f"Your score is {score}") 
   

### main quiz program.  Includes entry validation using a while loop
### loops through all questions, then calls checkans() function, passsing
### index and user answer

q_num = 0

def start_quiz():
    global entered
    
    for i in q_and_a:   # loop through dict
        print(i)            # i represents key (question)
        print(q_and_a[i])       # this represents value (all possible answers)
        user_input = ""         
        while user_input.upper() not in ["A", "B", "C", "D"]:       # validate entry
            user_input = input("enter a letter to answer the question  ")
        check_ans(q_num, user_input.upper())
        


### implement loop for quiz using a while condional

do_again =True

while do_again == True:
    start_quiz()
    reply = input("Play again?  y/n")
    if reply.upper() != "Y":
        do_again = False
        print("Goodbye !")

