from youtube_dl import YoutubeDL
from youtube_search import YoutubeSearch
from logger import throw_error
from functions import *
import os
import pyfiglet



if __name__ == "__main__":

    os.system("clear")
    pyfiglet.print_figlet('PipeCat', colors="RED")
    action = input(">> ")
    print("")
    search_results = []


    while not action == "quit" and not action == "q":
       
        if action.startswith("search"):
            search_results = search(action.split(" ", 1)[1])

        if action.startswith("play"):
            play(args = action.split(" ", 1)[1], search_results=search_results)
        
        if action.startswith("cd"):
            search_results = change_directory(args = action.split(" ", 1)[1], search_results = search_results)

        if action.startswith("mklist"):
            make_list(action.split(" ")[1])

        if action.startswith("list"):
            if " " in action:
                print_list(action.split(" ")[1])
            else:
                print_lists()

        if action.startswith("add"):
            add_to_list(action.split(" ", maxsplit=1)[1], search_results)

        if action.startswith("clear"):
            os.system("clear")

        print("")
        action = input(">> ")
        print("")

