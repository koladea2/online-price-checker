import requests
import random
from random import randint


def get_json(amount, category, difficulty):
    url = "https://opentdb.com/api.php?amount=" + 
            str(amount) + "&category=" + str(category) + 
            "&difficulty=" + str(difficulty)
    response2 = requests.get(url)
    file = response2.json()
    return(file)


def introduction():
    print("Hello, Welcome to TRIVIA!")
    print("----------------------------------------")
    print("GAME INSTRUCTIONS")
    print("Use the number pad to choose options.")
    start_game = input("To start the game, type START : ")

    return start_game


def display_ids():
    dictionary = {9: "General Knowledge", 10: "Entertainment: Books",
                  11: "Entertainment: Film", 12: "Entertainment: Music",
                  13: "Entertainment: Musicals & Theatres",
                  14: "Entertainment: Television",
                  15: "Entertainment: Video Games",
                  16: "Entertainment: Board Games",
                  17: "Science & Nature", 18: "Science: Computers",
                  19: "Science: Mathematics", 20: "Mythology", 21: "Sports",
                  22: "Geography", 23: "History", 24: "Politics", 25: "Art",
                  26: "Celebrities", 27: "Animals", 28: "Vehicles",
                  29: "Entertainment: Comics", 30: "Science: Gadgets",
                  31: "Entertainment: Japanese Anime & Manga",
                  32: "Entertainment: Cartoon & Animations"
                 }
    
    for (key, value) in dictionary.items():
        print(key , value)
        
    print("\n")
    category_choice = input("Choose a category using the number options above: ")
    return(category_choice)

  
def game_difficulty():
    third_decision = ""
    difficulties = {0 : "easy", 1 : "medium", 2 : "hard"}
    
    print("Select a difficulty: ")
    print("---------------------------------------")
    print("0 : Easy")
    print("1 : Medium")
    print("2 : Hard")
    print("\n")    
  
    users_difficulty = int(input("Choose a difficulty: "))
    if users_difficulty < 0 or users_difficulty > 2:
        while users_difficulty < 0 or users_difficulty > 2:
            users_difficulty = int(input("please enter another difficulty: "))
            print(users_difficulty)
            if users_difficulty > 0 and users_difficulty < 2:
                break
    third_decision = difficulties[int(users_difficulty)]
    # print("game_difficulty function")
    # print(third_decision)
    return third_decision


# passing all the info from the API into a dictionary
def Api_to_dictionary(link):
    Dic = {}
    i = 0
    for item in link['results']:
        sub_dict = {}
        sub_dict["category"] = item["category"]
        sub_dict["type"] = item["type"]
        sub_dict["difficulty"] = item["difficulty"]
        sub_dict["question"] = item["question"]
        sub_dict["correct_answer"] = item["correct_answer"]
        sub_dict["incorrect_answers"] = item["incorrect_answers"]
        Dic[i] = sub_dict
        # Dic[i] = item["category"], item["type"], item["difficulty"], item["question"], item["correct_answer"], item["incorrect_answers"]
        i = i +1
    return Dic


# printing only the question that fit to the user specifications
def print_questions(Dic):
    good_points = 0
    print("This is the dictionary")
    print(Dic)
    for item in Dic.values():
        print("------------------------------------------------------------------")
        print(item["question"])
        print("\n")
        check = item["type"]
        print(check)
        #print("[" + str(item["correct_answer"]) + ", " + str(item["incorrect_answers"][0]) + ", " + str(item["incorrect_answers"][1]) + ", " + str(item["incorrect_answers"][2] + "]"))
        if check == "multiple":
            print("[" + str(item["correct_answer"]) + ", " + str(item["incorrect_answers"][0]) + ", " + str(item["incorrect_answers"][1]) + ", " + str(item["incorrect_answers"][2] + "]"))
        else:
            print("[" + str(item["correct_answer"]) + ", " + str(item["incorrect_answers"][0] + "]"))
       
        print(item["correct_answer"])
        # For multiple choice, enter the answer in single quotes
        answer = (input("And your answer is: ")).lower()
        #print("It works!")

        if answer == (item["correct_answer"]).lower():
            print("######################################################")
            print("Nice! Good Job")
            good_points = good_points + 1
        else:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print("Keep trying!")
      
        print("\n")
                
    return good_points 


def main():
    #FirstChoice = introduction()
    num_questions = "10"
    category_choice = display_ids()
    print("\n")
    difficulty_choice = game_difficulty()
    print("\n")
    link = get_json(num_questions, category_choice, difficulty_choice)
    dictionary = Api_to_dictionary(link)

    print("------------------------------------------------------------------------------------------------")
    
    good_points = print_questions(dictionary)
    
    print("Total points: ", good_points)
 

main()
