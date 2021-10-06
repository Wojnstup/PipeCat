from logger import throw_error
from functions import *
from manual import * 
import os
import pyfiglet



if __name__ == "__main__":

    os.system("clear")
    pyfiglet.print_figlet('PipeCat', colors="RED")
    action = input(">> ")
    print("")
    search_results = []


    while not action == "quit" and not action == "q":

        if not " " in action or action.startswith(" "): #or action.endswith(" "):
            invalid_input = True
        else:
            invalid_input = False
       
        if action.startswith("search"):
            if invalid_input:
                throw_error("INVALID INPUT")
            else:
                search_results = search(action.split(" ", 1)[1])

        if action.startswith("play"):
            if invalid_input:
                throw_error("INVALID INPUT")
            else:
                play(args = action.split(" ", 1)[1], search_results=search_results[:])
        
        if action.startswith("cd"):
            if invalid_input:
                throw_error("INVALID INPUT")
            else:
                search_results = change_directory(args = action.split(" ", 1)[1], search_results = search_results)

        if action.startswith("mklist"):
            if invalid_input:
                throw_error("INVALID INPUT")
            else:
                make_list(action.split(" ")[1])

        if action.startswith("list"):
            if " " in action:
                if action.endswith(" "):
                    throw_error("INVALID INPUT")
                else:
                    print_list(action.split(" ")[1])
            else:
                print_lists()

        if action.startswith("add"):
            if invalid_input:
                throw_error("INVALID INPUT")
            else:
                add_to_list(action.split(" ", maxsplit=1)[1], search_results)

        if action.startswith("clear"):
            os.system("clear")

        if action.startswith("remove"):
            if invalid_input:
                throw_error("INVALID INPUT")
            else:
                remove_song(action.split(" ", maxsplit=1)[1])

        if action.startswith("man"):
            print_manual()

        print("")
        action = input(">> ")
        print("")

