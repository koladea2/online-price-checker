import requests
import random
from random import randint 

def get_json():
    url = "https://opentdb.com/api.php?amount=50"
    response2 = requests.get(url)
    file = response2.json()
    return(file)


def introduction():
    print("Hello, Welcome to Trivia!")
    print("----------------------------------------")
    print("GAME INSTRUCTIONS")
    print("Use the number pad to choose options.")
    start_game = input("To start the game, type START : ")
    
    return start_game
    

def game_options():
    Final_decision = ""
    General_category = {'0' : "All", '1' : "Entertainment: ", '2' : "Science & Nature: ", '3' : "Mythology", '4' : "History", '5' : "Celebrities", '6' : "Politics", '7' : "Art", '8' : "Animals", '9' : "General Knowledge"}
    print("0 : Any category")
    print("1 : Entertainment")
    print("2 : Science")
    print("3 : Mythology")
    print("4 : History")
    print("5 : Celebrities")
    print("6 : Politics")
    print("7 : Art")
    print("8 : Animals")
    print("9 : General Knowledge")
    
    users_category = input("Choose a category: ")
    
    #if user selected 0
    if users_category == 0:
        random_number = randint(1,9)
        users_category = random_number
        
    #if user selected 1 or 2
    elif users_category == 1 or users_category == 2:
        sub_category = category_options(users_category)
        Final_decision = General_category[users_category] + sub_category #Look in the dictionary and return the option selected with the subcategory
      
    #if selection was any number > 2  
    else:
        Final_decision = General_category[users_category]    #Look in the dictionary and return the option selected
    
    return Final_decision
  
  
def category_options(users_category):
    second_decision = ""
    Second_category1 = {'0' : "Books", '1' : "Film", '2' : "Music", '3' : "Television", '4' : "Video games", '5' : "Board games", '6' : "Cartoons & animations", '7' : "Anime & Manga", '8' : "Comics", '9' : "Musicals & Theaters"}
    Second_category2 = {'0' : "Computers", '1' : "Mathematics", '2' : "Gadgets"}
      
    if users_category == 1:
        print("Select a category: ")
        print("---------------------------------------")
        print("0 : Books")
        print("1 : Film")
        print("2 : Music")
        print("3 : Television")
        print("4 : Video games")
        print("5 : Board games")
        print("6 : Cartoons & Animations")
        print("7 : Anime & Manga")
        print("8 : Comics")
        print("9 : Musicals & Theaters")

        entertainment_choice = input("Choose an option : ")
        second_decision = Second_category1[entertainment_choice]
        return second_decision
      
      
    elif users_category == 2:
        
        print("Select a category: ")
        print("----------------------------------------")
        print("0 : Computers")
        print("1 : Mathematics")
        print("2 : Gadgets")
        
        entertainment_choice = input("Choose an option : ")
        second_decision = Second_category2[entertainment_choice]
        return second_decision
    
    #re-locate this statement 
    else:
        print("Incorrect input! Please choose from the above options")
        
      

def game_difficulty():
    third_decision = ""
    Difficulties = {'0' : "Easy", '1' : "Medium", '2' : "Hard"}
    
    print("Select a difficulty: ")
    print("---------------------------------------")
    print("0 : Easy")
    print("1 : Medium")
    print("2 : Hard")
    
    users_difficulty = input("Choose a difficulty: ")
    third_decision = Difficulties[users_difficulty]
    return third_decision


def game_type():
    fourth_decision = ""
    Types = {'0' : "boolean", '1' : "multiple"}
    
    print("Select a game type: ")
    print("---------------------------------------")
    print("0 : True or False")
    print("1 : Multiple choice")
    
    users_type = input("Choose a game type: ")
    fourth_decision = Types[users_type]
    return fourth_decision
    
        
    return users_type


#passing all the info from the API into a dictionary
def Api_to_dictionary(link):
    Dic = {}
    i = 0
    for item in link['results']:
        Dic[i] = item["category"], item["type"], item["difficulty"], item["question"], item["correct_answer"], item["incorrect_answers"]
        #print(Dic[i])
        i = i + 1

    return Dic


#printing only the question that fit to the user specifications
def print_questions(Dic, option1, option2, option3):
    total_points = 0
    good_points = 0
    i = 0  
    for item in Dic[i]:
        if item["category"] == option1 and item["type"] == option2 and item["difficulty"] == option3:
            total_points = total_points + 1
            print(item["question"])
            print(item["correct_answer"] + ", " + item["incorrect_answers"])
            print("And the answer is: " )
            answer = input()
            if answer == item["correct_answer"]:
                print("Nice")
                good_points = good_points + 1
            else:
                print("Keep trying!")
        i = i + 1
                
    return total_points, good_points
        

    
def main():
    #FirstChoice = introduction()
  
    link = get_json()
    dictionary = Api_to_dictionary(link)
    
    category_choice = game_options()
    difficulty_choice = game_difficulty()
    type_choice = game_type()
    
    print(dictionary)
    print("------------------------------------------------------------------------------------------------")
    print(category_choice) #0 fails, 1 ans 2 fail to send to other function 
    print(difficulty_choice) #good
    print(type_choice) #good
    #everything work up to here
    
    total_score, good_points = print_questions(dictionary, category_choice, difficulty_choice, type_choice)
    
    print(total_score)
    print(good_points)
    
    

main()

