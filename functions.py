from youtube_dl import YoutubeDL
from youtubesearchpython import VideosSearch, ChannelSearch, PlaylistsSearch, ChannelsSearch, Playlist
from logger import throw_error
import os
import playlists

### CONFIG ###
max_results = 10
ydl_opts = {}

def search(command):
    if " " in command:
        query = command.split(" ", 1)[1]
    else:
        throw_error("Bad usage - use 'search playlist' or 'search audio' or 'search channel'")
        return []

    index = 1
    search_results = []

    if command.startswith("audio"):
        results = VideosSearch(query=query, limit=max_results).result()["result"]
        for i in results:
            print(str(index) + ". " + i['title'] + " - " + i["channel"]["name"])
            

            search_results.append("https://www.youtube.com/watch?v=" + i['id'])
            index = index + 1

    elif command.startswith("channel"):
        results = ChannelsSearch(query=query, limit=max_results).result()["result"]
        for i in results:
            print(str(index) + ". " + i['title'])
            
            channels = ChannelsSearch(query=query).result()["result"]
            for channel in channels:
                playlist_id = channel["id"]
                playlist_id = playlist_id[0:1] + "U" + playlist_id[2: ]
                url = "https://www.youtube.com/playlist?list=" + playlist_id
                search_results.append(url)

            index = index + 1
    elif command.startswith("list"):
        results = PlaylistsSearch(query=query, limit=max_results).result()["result"]
        for i in results:
            print(str(index) + ". " + i['title'] + " - " + i["channel"]["name"])
            search_results.append("https://www.youtube.com/playlist?list=" + i['id'])
            index = index + 1

    else:
        throw_error("Bad usage - use 'search playlist' or 'search audio' or 'search channel'")
        return []

    return search_results


def play(args, search_results = []):
    if args.startswith("index"):
        if search_results == []:
            throw_error("SEARCH FOR SOMETHING FIRST")
            return
        try:
            #print(len(search_results))
            if int(args.split(" ")[1]) > len(search_results) or int(args.split(" ")[1]) <= 0:
                throw_error("INDEX OUT OF RANGE")
                return
            
            if "shuffle" in args:
                first_link = search_results[int(args.split(" ")[1]) - 1 ]
                search_results.remove(first_link)
                playlists.random.shuffle(search_results)
                search_results = [first_link] + search_results

            if "nostop" in args:
                index = 1 
                for link in search_results:
                    if index >= int(args.split(" ")[1]):
                        if "video" in args:
                            os.system("mpv " + str(link))
                        else:
                            os.system("mpv " + str(link) + " --no-video")
                    index = index + 1


            else:
                if "video" in args:
                    os.system("mpv " + str(search_results[int(args.split(" ")[1]) - 1 ]))
                else:
                    os.system("mpv " + str(search_results[int(args.split(" ")[1]) - 1 ]) + " --no-video")

        except:
            throw_error("GIVE A VALID INDEX")
            return
    elif args.startswith("list"):
        args = args.split(" ", maxsplit=1)[1]
        list_args = args.split(" ")

        name = list_args[0]
        start = -318
        shuffle = False


        for argument in list_args:
            if "index" in argument:
                start = int(argument.replace("index", ""))
            if argument == "shuffle":
                shuffle=True
 

        playlist = playlists.get_list(name)
        if "video" in args:
            playlists.play_list(list=playlist, start=start, shuffle=shuffle, video=True)
        playlists.play_list(list=playlist, start=start, shuffle=shuffle)

    else:
        try:
            if "video" in args:
                os.system("mpv " + args)
            else:
                os.system("mpv " + args + " --no-video")
        except:
            throw_error("GIVE A VALID URL")
    
def change_directory(args, search_results=[]):
    if search_results == []:
        throw_error("Search for something first!")
        return
    
    contents = []
    try:
        results = Playlist(search_results[int(args) - 1]).videos
        index = 1
        for video in results:
            print(str(index) + ". " + video['title'] + " - " + video["channel"]["name"])
            contents.append("https://www.youtube.com/watch?v=" + video["id"])
            index = index + 1
        return contents
    except:
        print("Syntax: 'cd 2'")
    
    return search_results
       
def make_list(name):
    if " " in name:
        throw_error("NO SPACES ALLOWED")
        return
    playlists.create_playlist(name)

def print_list(name):
    index = 1
    try:
        for song in playlists.get_list(name):
            print(str(index) + ". " + song[0])
            index = index + 1
    except:
        return

def print_lists():
    lists = playlists.get_lists()
    index = 1
    for name in lists:
        print(str(index) + ". " + name)
        index = index + 1
    
def add_to_list(args, search_results = []):
    if not args or not " " in args:
        throw_error("Syntax: 'add <playlist name> <url>' or 'add <playlist_name> index <index>'")

    args = args.split(" ")
    link = ""
    if args[1] == "index":
        try:
            link = search_results[int(args[2]) - 1]
        except:
            throw_error("GIVE A VALID INDEX")
    else:
        link = args[1]

    title = input("Give the song a title: ")
    playlists.add_song(list_name=args[0], song_title=title, song_url=link)

def remove_song(args):
    if not " " in args:
        throw_error("Syntax: 'remove <list_name> <song_name>'")

    arguments = args.split(" ", maxsplit=1)
    list_name = arguments[0]
    song_name = arguments[1]

    print("You are about to remove {song} from {list_name}.".format(song=song_name, list_name=list_name))
    if input("Print 'yes' if you're sure: ") == "yes":
        playlists.remove_song_from_list(list_name, song_name)