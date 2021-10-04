import pyfiglet

def print_manual():
    pyfiglet.print_figlet("Usage", colors="RED")
    print("Ignore the <>, example: play index <index> -> play index 4")
    print("If something is in {} like {shuffle} or {video} it's an optional argument")
    print("")
    print("Searching:")
    print("  search audio <query>   <- searches for videos on Youtube")
    print("  search channel <query>   <- searches for Youtube channels and music topics")
    print("  search list <query>   <- searches for playlists on Youtube")
    print("  cd <index>   <- replaces your search results with either contents of a playlist or a channel from search results")

    print("")
    print("")

    print("Play:")
    print("  play <url> {video}  <- plays an url audio. This doesn't have to be a Youtube url. It will play audio only unless you type in video")
    print("  play index <index> {video}  <- plays an index of a search query. You find those indexes after you search for something.")
    print("  play list <name_of_list> index<index> {shuffle}   <- plays from offline playlist <name_of_list> starting on index <index> and there's an option to shuffle. Notice no space between index and <index>")

    print("")
    print("")

    print("Offline playlists:")
    print("Disclaimer! These playlists don't download any songs or videos. You need internet to listen to them.")
    print("They are called 'offline', because you don't actually make a Youtube playlist")
    print(" ")
    print("  mklist <name>   <- creates an offline playlist in 'data/playlists.db'")
    print("  list   <- prints the names of all your offline playlists")
    print("  list <name>   <- prints the contents of an offline list. You can then play any song from it with 'play index <index> {video}'")
    print("  add <name_of_list> index <index>  <- add a song with a given index to a playlist")
    print("  remove <list_name> <song_name>  <- remove a song from a list")

    print("")
    print("")

    print("  man  <- print this manual")