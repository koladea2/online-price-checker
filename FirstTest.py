import requests
import randint 

def get_json()
    url = "https://opentdb.com/api.php?amount=50"
    response2 = requests.get(url)
    file = response2.json()
    return(file)


def game():
    print("Hello, Welcome to Trivia!")
    print("----------------------------------------")
    print("GAME INSTRUCTIONS")
    print("Use the number pad to choose options.")
    start_game = input("To start the game, type START : ")
  

def game_options():
    Final_decision = ""
    General_category = ["All", "Entertainment: ", "Science & Nature: ", "Mythology", "History", "Celebrities", "Politics", "Art", "Animals", "General Knowledge"]
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
    return users_category
  
  
def category_options(users_category):
    #Final_decision = General_category[users_category]
    #return = Final_decision
    #start new function?
    #process for Any category (rand_num from 1-9)
    if users_category == 0:
        random_number = range (1, (randint * 9))
        users_category = random_number
      
    elif users_category == 1:
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
      
    elif users_category == 2:
        print("Select a category: ")
        print("----------------------------------------")
        print("0 : Computers")
        print("1 : Mathematics")
        print("2 : Gadgets")
        
#     elif users_category == 3:
#     elif users_category == 4:
#     elif users_category == 5:
#     elif users_category == 6:
#     elif users_category == 7:
#     elif users_category == 8:
#     elif users_category == 9:
    
    else:
        print("Incorrect input! Please choose from the above options")
        
  Final_decision = General_category[users_category]
      

def game_difficulty():
    print("Select a difficulty: ")
    print("---------------------------------------")
    print("0 : Easy")
    print("1 : Medium")
    print("2 : Hard")
    
    users_difficulty = input("Choose a difficulty")
    return(users_difficulty)
      



def game_type():
    print("Select a game type: ")
    print("---------------------------------------")
    print("0 : True or False")
    print("1 : Multiple choice")
    users_type = input("Choose a game type")
    
    #convert the user input of option3 into the same language of the API
    if users_type == "true or false":
        users_type = "boolean"
    else:
        users_type = "multiple"
        
    return users_type
  
#print all posible category
#Chosee the category(user_input)
#option1 = input()
#Chosse the dificulty(user_input)
#print the 3 difficultyes
#option2 = input()
#choose the game type(user_input)
#print true or false & multiple choice
#option3 = input()



#passing all the info from the API into a dictionary
def Api_to_dictionary():
    Dic = {}
    i = 0
    for item in file['results']:
        Dic[i] = item["category"], item["type"], item["difficulty"], item["question"], item["correct_answer"], item["incorrect_answers"]
        #print(Dic[i])
        i = i + 1

    return Dic


#printing only the question that fit to the user specifications
def print_questions():
    total_points = 0
    good_points = 0
    i = 0  
    for items in Dic[i]:
        if item["category"] == option1 && item["type"] == option2 && item["difficulty"] == option3:
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
                
    return total_points, good_points
        

    
def main()
    game()

    if start_game.lower() == "start":
         game_options()
    

