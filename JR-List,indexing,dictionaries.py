#Jose R. Rodriguez
#date: 10-20-2020
#Class: Python Programming 1
#CSC235
#Teacher: Tony Hinton
#Assignment: Lists, indexing, dictionaries, and other common data structures
#---------------------------------------------------------------#
 
#This is a program / tutorial to show how to use variables
#How to combine variables & print out the ouput

#_______________________________________________________________#
#now that we have learn how to assigned values to variable, combined variables & print variables
# lets put it all to practice in the following example:
#It is a small program that has a message and display my name, last name & my age.
#we are going to used everything with learn:

 
x = "Jose" #Variable with my first name, a string
y = " Rodriguez" #variable with my last name, a string
a = 35 #variable with my age, an interge
print("*********-Welcome to Python Tutorial-**********\n") # Welcome message
n = x+y #variable with a combination of to variables
print ("Hello my name is " + n ) #display welcome message and my name
print ("I am " + str(a) + " years old.")#display my age
print ("I will be your guide thru this program") #display message
#NOTE: to combine string & interge together you will have to change the interge value to a string
#For that we will have to use the string command (str) so it will be written str(a), which is equal to str(35)
print ("Yes, I know " + x + " is the most common Spanish name ever!!!!")#display message & my name
print ("And" + y + " the most common last name too.\n") #display my last name & message

input("Press Enter to continue with the tutorial...")

T= """\nIn this tutorial you will learn how to assigned a value to a variable
for example if I have a variable x and I want to assigned a string I will do using the (=) sign
x = "Jose"(string) and the string is written in quotation marks"

If I want to assign a intergen to a variable I would use the (=) sign as well
a = 35(interge) but notice for interges with don't need to use quotations mark

if I want to combine to values or variables together I would use the (+) sign
for example if I have a variable x with a string "jose" and a variable y with a string "Rodriguez"
I can combined the variable and values by doing: x + y

Now if you want to combine those variables into a single variable it could be represent it like this:
n = x + y, which is equal n = "Jose" + "Rodriguez"

Finally if I want to print something or display anything in the monitor I would have to use the command (print)
For example: print ("hello my name is")
Notice that the elements to be display by the print command has to be in () parentheses
print commmand has to be lower case
Also as with stablished strings has to be inside quotation marks ""

now if I want to print the values of variable if could be written like this:
print(x) which it is the same as doing: print("Jose"), so it will display:
Jose (on the screen)

the same method apply to a interge value
if want to print a variable a with a value of 35 : a = 35, it will be written:
print (a), which is equal to print(35), it will display:
35 (on the screen)\n\n"""
print (T)

#_______________________________________________________________________________#


input("Press Enter to continue with the tutorial...")

T2 = """\n#________________________________________________________________________________________________________#
In this next chapter of this tutorial we are going to develop how to insert and output user information
#How to pass the user input either string or interge data type

#We are going to use a specific command to get user information which is (input)
# As simple as that (input) is to get the user input
#And of course if we want to display the user input we will use the (print) command

# lets say that I want to get the user's name, the code will be writen:

# uname = input("what is your name?")

#output - what is your name?
#if the user write's Pablo
#then usame = "Pablo"

# uname - is going to be the variable that will hold the user input
# input - is the command to get the user input
# "what is your name?" - is the string that is going to be display for the user to see, so they can put their information required
#NOTE: remember string has to be in quotation marks ""

#To display the user input we will use the print command, so the code will be written:

#print("Hello " + uname)
#which it will display: hello Pablo

#print - is the command to display ouput to the monitor
#"hello" - is a string message
#(+) - is the symbol to combine the string message & user input
#uname - is the varible holding the user input

#Now lets say that I want to do the same but you want to hold a interge in the variable
#The code will be written:

#uage = input("How old are you?")

#uage - is the variable to hold the user input
#input - is the command to get the user input
#"How old are you? " - is the string message to diplay to the users to get their information. Note: string in quotation marks ""

#display - how old are you?
#if the user enter 25
#then uage = 25

#To display the user input we will use the print command, so the code will be written:

#print("So you are " + uage + " years old")
#display - So you are 25 years old

#print - command to display information to the monitor
#"So you are" - first line string message
#uage - variable holding user input which is 25
#"years old" - second line string message\n\n"""

#______________________________________________________________________________________________________________#
#Now that we know how to use input and output let's have some fun
#Let's add and improve our program
print(T2)
uname = input ("What is your name? ") #getting user input
print("******** Welcome " + uname + " **********") #displaying welcome message and user input
uage = input("\nhow old are you? ") # getting user input most like to be and interge. Note: (\n) is to make a new line or display anything that you write in a new line
print ("So you are " + uage + " years old") #displaying user input and messages


#I am adding a if statement to make things more fun
if int(uage) < 30: #if statement, to be able to compare the user input with an interge we have to make sure that the input is an interge that its why is written: int(uage)
    print("Wow you are a youngster") # display message if user input is less than 30 

elif int(uage) > 30: #else if statement to display a message if user input is more than 30, we have to convert user input as an interge as well: int(uage)
    print("\nWell, someone needs a senior citizen card, hahahhahaha just kidding") # display message if user input is more than 30
        
if_u_correct = False # variable holding a boolean for a while loop
while if_u_correct == False: # while loop statement
    
    print ("\nLet's check if you know a little bit of math")#display message
    uanswer = input ("How much is: 2 + 2 + 2 - 2 = ")#getting user input to whole in the uanswer variable which will be and interge
    ranswer = 4 # right answer to compare with user input answer

    if int (uanswer) == ranswer: # if statement to check if user input has the right answer
        print("\nYou know your math, what are you doing here? shouldn't you be teaching math at some school.") # display message if user enter the right answer
        if_u_correct = True

    elif uanswer != ranswer:# elif statement if the user input is not the right answer
        print ("\n*******-Sorry that is not the answer-*******") # display message is user enter wrong answer
        print ("\nWell, we are going to have to send somenone back to the first grade!\n") #display funny message when user enter wrong answer
        if_u_correct = False

T3="""\n#__________________________________________________________________________________________________________________________#
#I used a few if statement in this tutorial just to make things more fun and a while loop
#let start with the while loop
# first what is a loop, & what with you use it
#A loop you whould use it to return to a certain part of the program until something is complete to break the loop
#For example I asked you a math question:
#how much is : 2+2+2-2 =, the right answer is 4
#So I created a while loop to go back to the same question until you give me the right answer
#how I did that?

#I set a variable holding a boolean if_u_correct = False
#then I set the while loop statement: while if_u_correct== False

#for all that to work there is a few more steps to do, we need to put some if statements and make sure that the code is inside the while loop
#let start with the if statement

#if statement is use to compare parts in the program and take action depending on the user respond or action
#For example: back to the math question 2+2+2-2 = 4
#We will said if the user answer is 4 print this("You know your math, what are you doing here? shouldn't you be teaching math at some school.")

#then we will need a elif statement too, to stablish if the user doesn't write the right answer the program to somenthing else
#elif user answer is not 4 print this ("*******-Sorry that is not the answer-*******")
#Then the while loop will take control and send back the user to the same math question until the user gets the right answer

#Since the while loop is working with a boleean
#We have to make sure that we put boleean for the if & elif statement to stablish what is the right answer
#The code will be written the following:

if_u_correct = False 
while if_u_correct == False: 
    
    print ("\nLet's check if you know a little bit of math")
    uanswer = input ("How much is: 2 + 2 + 2 - 2 = ")
    ranswer = 4 

    if int (uanswer) == ranswer: 
        print("\nYou know your math, what are you doing here? shouldn't you be teaching math at some school.") 
        if_u_correct = True

    elif uanswer != ranswer:
        print ("\n*******-Sorry that is not the answer-*******") 
        print ("\nWell, we are going to have to send somenone back to the first grade!\n") 
        if_u_correct = False

#NOTE: One more thing for the code to work in the while loop, we have to make sure that we put the code in a code block
#How do we do that?
#We have to make sure that the code inside the while loop is tab over for the code to work\n"""

print(T3) #display tutorial to the user
#Well now that we know how to implement if statements and while loop lets have some fun

is_u_rcolor = False #variable holding the boleean for the while loop
while is_u_rcolor == False: #while loop statement
    r_color = "purple" #variable holding the right answer
    u_color = input("What color do you get by mixing red & blue? ") #variable holding display question to get user input
    print("if you need a hint write the word 'hint'\n") # display option for the user to get a hint
    hints = ["\n1) Starts with P\n", "2) It's Barney's color\n", "3) It is part of the rainbow colors\n"] # list of hints

    if u_color == r_color: #if statement comparing to the right asnwer
        print("\nI guess you are an artist to know the colors palette\n") #display if the user gets the right answer
        is_u_rcolor = True # boleean if the user pick the right answer to stop the while loop

    elif u_color == "hint": # elif statement if the user choose hints
        for each_hint in hints: #for loop to go thru the list
            print(each_hint) #display list
        is_u_color = False # boleean to go back to loop if the user gets the answer wrong

    else: #else statement
        print("\n*****-Wow that is not the correct answer-******, back to kindergarden!!!!!!!!\n") #display if user gets answer incorrect
        is_u_color = False # boleean to go back to loop if the user gets the answer wrong

input("Press Enter to continue with the tutorial...")

is_u_ranimal = False # variable to holding a boleean for the while loop
while is_u_ranimal == False: # while loop statement
    r_animal = "tigre" # variable holding the right answer
    u_animal = input ("\nWhat kind of animal looks like a cat but is fierce? ") # variable holding message for user to get input
    print ("If you want a clue write the word 'clue'\n") #display message if user wants a clue
    clues = ["\n1- they are bigger cats","\n2- they are cousins of the Lion"] # clues list
    mclues = ["\n3-their name start with the letter T", "\n4-They most likely live in the wild"] # more clues list
    more = mclues #variable holding the more clues list
    

    if u_animal == r_animal: # if statement
        print ("\nOnly a fierce animal would know another fierce animal, gaaaarrrrr\n") #Display if user gets the right answer
        is_u_ranimal = True #boleean to break the loop when the answer is correct

    elif u_animal == "clue": # elif statement
        for eclue in clues: # for loop to get the list of clues
            print(eclue) # display list of clues
            u_more = input("if you like more clues write 'more'\n") # variable to hold input if the user wants more clues
            if u_more == "more": # if statement to get user to get more clues
                for more_clues in mclues:#for loop to get the more clue lis
                    print(more_clues) #display more clues list
                    if u_more == r_animal: # if statement if the user get answer right to break the loop
                        is_u_ranimal = True
                    else:
                        is_u_ranimal = False # else statement when user gets answer wrong

    else: # else statement when user gets answer wrong
        print ("-------Soooorrrryyyyyy-------- that is not the correct answer, Animal planet is a good way to start learning about animals") #display id user gets answer wrong
        is_u_ranimal = False #boolean to stablish the answer is wrong

input("Press Enter to continue with the tutorial...")
print("\n*-----------------------------------------------------------------------------------------------------------------------*\n")

T4 = ("""#Now in this part of this python tutorial we are going to go over some data structures
Let's start with a List. What is a list?
A list basically is set of values that you contain on a variable.
It is like it says is a list. So for example:
If we have grocery list, let's say that we need bananas, chicken, bread, rice, coffee and icecream.
Grocery - will be the variable holding the list.
bananas, chicken, bread, rice, coffee and icecream are the items or values in the list.
how do we write that?
\nGrocery = ["bananas", "chicken", "bread", "rice", "coffee", "icecream"] - NOTE: items in a list are in a square braket and separated by commma

To print the list will be simple like this:
print(grocery)
the ouput will be: bananas chicken bread rice coffee icecream

Now that we got that part cover, there is a lot of things we can do with a list.
We can add items to the list, we can remove items, we can clear the list and we can even loop thru the list.
We use different methods for that.
Let's say that we have our Grocery list above and we want to add an item. the code will be written the following:
\ngrocery.append("orange juice")
grocery is our list variable, append is the command that we use to add items to the list and orange juice is item that we are adding.
NOTE: since we are using a command for the list the item will be in parenthesis()

now if we want to remove and item for the list will be use the command remove
the code will be written:

Grocery.remove("bananas")

if we want to loop thru the list, the code will be written:
for G in Grocerie:
print (G)

output will be:
chicken
bread
rice
coffee
icecream
orange juice

Now that we know how to use a list lets have some fun\n\n""")
print (T4)


print ("\nHey what do you think if we make a sangria! \n")# display message to the user
print ("I already had red wine, white wine, lemon & ice\n")# display message to the user
sangria =["Red Wine", "White Wine", "Ice", "Lemon"] #make a list
u_fruit = input("What kind of fruit would you like to add? ") #getting user input
sangria.append(u_fruit) #adding user input to the list
u_fruit = input ("add another fruit, please: ") #getting another input from the user
sangria.append(u_fruit) #adding the second input from the user
print ("\nSangria ingredients ", sangria) #display message & sangria list

is_sangria = False #stablish variable holding a boolean for while loop
while is_sangria == False: # created a while loop
    u_wine = input ("\nWhat kind of wine would you like red or white? ") #getting user input
    if u_wine == "red": #if statement if the user choose red to do something
        sangria.remove("White Wine") #removing item from the list
        print ("\nOk your ingredients are: ",sangria) #display message & list
        is_sangria = True #boleean to break the while loop returning true

    elif u_wine == "white": # elif statement if the user choose white to do something
        sangria.remove("Red Wine") #removing item from the list
        print ("\nOk your ingredients are: ",sangria) #display message & the list
        is_sangria = True #boleean to break the while loop returning true

    else: #else statement if the user put the wrong answer to do something
        print("\nSorry that is not the correct answer") # display message
        is_sangria = False #boleean to continued the while loop returning false

u_remove_fruit = input ("I think we have a lot of fruit, can you remove a fruit please?, choose fruit to remove: ") #display message for the user to remove fruit
sangria.remove(u_remove_fruit.casefold()) # removing item from the fruit list
print ("\nOk so the final ingredients for your sangria are: ", sangria) # display message and fruit list

print ("\nNow that we have a delicious sangria, we can't drink with an empty stomach!") #display message
sea_food = ["1)Lobster"," 2)Shrimp", "3)Cod fish", "4)Scallops"] #creating a seafood list
u_food_answer = input ("\nWould you like to see what I am offering for food, I have seafood, yes or no? ") #getting user input
if u_food_answer == "yes": # if statement if the user choose yes to do something
    print ("We have: ", sea_food) # display the seafood list
    u_sfood_choice = input("\nWhat would you like? ") #getting user input to choose an item from the list
    sea_food.clear() # clearing the list
    sea_food.append(u_sfood_choice) # adding user input to the list
    print("You chose:",sea_food) #display the list with the user input
elif u_food_answer == "no": #elif statement if the user choose no to do something
    print("\nWell, I guess someome is going to get typsy and is not me!!!!!") #display message
    sea_food.clear() #clear the seafood list

is_pasta = False # variable to hold a booleanfor the while loop
while is_pasta == False:#while loop 
    print("The seafood comes with pasta, and even if you didn't choose any, you should eat something\n") # display message
    u_pasta_answer = input ("\nWould you like to know what we have for pastas, yes or no? ") #getting user input
    pasta = ['1)linguini ', "Tortellini ", "3)Spagueti ", '4)fusilli'] #creating a pasta list
    if u_pasta_answer =="yes": #if statement is the user choose yes to do something
        print("We have: ", pasta) #display list
        u_pasta_choice = input("\nWhat kind of pasta would you like? ") #getting user to choose wnat of the items in the list
        pasta.clear() #clearing pasta list
        pasta.append(u_pasta_choice) #adding user input to the list
        print ("You chose: ", pasta) #print the list with the user input
        is_pasta = True #variable with the boolean to break the while loop
    elif u_pasta_answer == "no": # elif statement if the user choose no to do something
        print ("\nWell, sorry you have to choose a pasta, drinking with an empty stomach is not aceptable\n") # display message
        is_pasta = False #variable with the boolean to continued the while loop

    else: #else statement
        print ("Sorry that is not the right answer") #display message
        is_pasta = False #boolean to continued the while loop
    
u_dinner = sea_food + pasta #join the 2 list together, the seafood list and the pasta list
print("\nYou have: ", len(u_dinner), "items to eat\n") #display message and the list amount of items in the list
print("\nYou dinner is: ", u_dinner) # display message and the join list

T5 = ("""\n\n Another data structure is Dictionaries
dictionaries are similar to a list but the variable would hold a list of keys & values
so is you a variable student and the key could be name & the value could be Joe
the code will be written the following:

student = {"name": "Joe"}

student - is the variable, name - is the key and Joe - is the value assigned to the name key
NOTE: dictionaries are created with curly brackets and the key and the value are separate by a colon

to display a dictionary you will use the method print
print(student)
output: name : Joe

to access just the value on a dictionary we will use the get() method.
the code will be written the following:

s = student.get("name")
print (s)

output: Joe

dictionaries are important if you want to specific values to a key
imaging when you go to doctor office, you information is put in a dictionary
Variable patience = {"name": ".....", "Last name": "......", "phone": "...........", "address": ".............."}

Now that we know how to use dictionaries, let's have son fun!!!!\n""")
print(T5)


print("\nHey!!!! now that we are having a nice food & sangria, I have to tell you something\n") #display message
print("\n I really believe in the zodiac signs\n") #display message
zodiac_month = {
    "January": "Capricorn",
    "February": "Aquarius",
    "March": "pisces",
    "April": "Aries",
    "May": "Taurus",
    "June": "Gemini",
    "July" : "Cancer",
    "August": "Leo",
    "September": "Virgo",
    "October": "Libra",
    "November": "Scorpio",
    "December": "Sagittarius"} #creating a dictionary
u_answer_count = input("Do you want to how many zodiac signs there is? yes or no: ")# getting user input
if u_answer_count == "yes": #if statement if the user input yes to do something
    print(len(zodiac_month), "zodiac signs") #display dictionary length and message
elif u_answer_count == "no": #elif statemnet is the user input no to do something
    print ("\nOK\n") #display message
    
print("\nWould you like to know the zodiac sign that corresponde by each month\n")#display message
u_sign_answer = input("yes or no? ") #getting user input to choose yes or no
if u_sign_answer == "yes": # if statement if the user choose yes to do something
    print("\nOK\n") #Display message
    for m,z in zodiac_month.items(): # creating a for loop to go thru the keys and values of the dictionary
        print(m, "-", z) #display dictionary

elif u_sign_answer == "no": #elif statement if the user choose no
    print("Ok, would you like me to tell you a least the sign by your month?\n") #display message
    user_sign = input("What is the month that you were born?\n") #getting user input
    s = zodiac_month.get(user_sign) # getting specific value depending of what the user input as a key
    print("Your sign is: ",s) #display message and dictionary value

    

        
    





