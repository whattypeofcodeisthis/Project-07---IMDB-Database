#!/usr/bin/env python
# coding: utf-8

# In[1]:


# First we write a function to import the data into a dictionary with actors as keys and movies as values because of the data structure

def first_dictionary():
    dic = {} 
    try:
        df = open("movies.txt","r")                   # first we open the given text file and read it
        following_line = df.readline().rstrip("\r\n") # We use rstrip to get rid of '/n' at the end of the last string in each line
        while (following_line != ""):                 # with the while function we will start to add to the dictionary
            line = following_line.split(", ")         # now we split the strings by the comma and remove the spaces
            actor = line[0]                           # here we select the actor as it is the first string in the line
            dic[actor] = line[1:]                     # here we add the actor as a key and the movies as values to the dictionary
            following_line = df.readline().rstrip("\r\n")          
    except:
        pass
    for key in dic:                                   # Now we change all values to lowercase because not all movies in the given file have the same capitalization structure
        if type(dic[key]) == type([]):                # This way the user can type in the movie titles in any way
            for index, item in enumerate(dic[key]):
                dic[key][index] = item.lower();
    return dic


# Now we will change the key to values and vice versa

def final_dictionary():
    dic = first_dictionary() 
    dic_final = {}
    for actor, movielist in dic.items(): 
        for movie in movielist:
            dic_final.setdefault(movie,[]).append(actor)
    return dic_final


final_dictionary()


# 1 - Find all actors

def actors_all(movie_1, movie_2):
    dic_final = final_dictionary()
    if movie_1 in dic_final.keys() and movie_2 in dic_final.keys():
        return set(dic_final[movie_1] + dic_final[movie_2]) 
    else:
        print("Movies are not in database")
        anykey = input("Enter any key to go back to the menu: ")
        menu()


# 1 - Find common actors

def actors_common(movie_1, movie_2):
    dic_final = final_dictionary()
    return set(dic_final[movie_1]).intersection(set(dic_final[movie_2]))
    


# 1 - Find difference

def actors_either(movie_1, movie_2):
    if len(actors_all(movie_1, movie_2)- actors_common(movie_1, movie_2)) > 0:
        return actors_all(movie_1, movie_2) - actors_common(movie_1, movie_2)
    else:
        return("There are no actors who are playing in the movies " + movie_1 + " and " + movie_2 + " but not in both movies")


# 2 - Find coactors

def co_actors(actor):
    coactors = []
    dic = first_dictionary()
    dic_final = final_dictionary()
    try:
        movies = dic[actor]
    except KeyError:
        print("Not in database")
        anykey = input("Enter any key to go back to the menu: ")
        menu()   
    for n in movies:
        if n in dic_final.keys():
            coactors += dic_final[n] 
    if len(coactors) == 1:                               # Check if there are co-actors. ==1 because actor still in list
        return "There are no co-actors"                 
    else:
        return set(coactors) - {actor}                   # deduce actor from list to show just coactors

    
# End
def end():
    end_input = input("Do you want to go back to the menu? (Y/N): ")
    if end_input.lower() == "y":
        print("Okay Then!")
        menu()
    elif end_input.lower() == "n":
        print("Okay Then! Come back soon!")
        quit()
    else:
        print("Invalid Input. You can only input y = yes or n = no!")
        end()
    
    
# Menu 
def menu():
    print( "Welcome to the IMDB Dictionary! \nPlease choose between the following two options (a/b): ")
    print("a: Find all the actors of two movies seperated by (&, |, ^)")
    print("b: Find all the co-actors of a given actor")
    selection = input("Enter your choice: ").lower()
    if selection == "a":
        movie_1 = input("Enter the name of first movie: ").lower()
        movie_2 = input("Enter the name of second movie: ").lower()
        allactors = actors_all(movie_1, movie_2)   
        commonactors = actors_common(movie_1, movie_2)
        eitheractors = actors_either(movie_1, movie_2)
        print("All actors who play in the movies", movie_1, "and", movie_2,"are:\n", allactors)
        if len(commonactors) > 0:
            print("The actors who are playing in both movies are:\n",commonactors)
        else:
            print("There are no actors playing in both", movie_1, "and", movie_2)
        print("All actors who are playing in the movies", movie_1, "and", movie_2,"but not in both movies are:\n", eitheractors)
        end()
    elif selection == "b":
        actor = input("Enter the name of an actor: ").title()
        allcoactors = co_actors(actor)
        print("All co-actors of", actor,"are:\n", allcoactors)
        end()   
    else:
        print("Invalid Choice. You can only enter a or b")
        anykey = input("Press any key to go back to the menu: ")
        menu()

# Intro
def intro():
    input_mario = input("Hey Mario, are you ready to test our kick ass code? (Y/N): ")
    if input_mario.lower() == "y":
        print("Buckle up and enjoy!")
        menu()
    elif input_mario.lower() == "n":
        print("We will just take the 6.0 then ;)")
        quit()
    else:
        print("Invalid Input. You can only input y = yes or n = no!")
        intro()
intro()


    


    

