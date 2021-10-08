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
    print("  play index <index> {video} {nostop} {shuffle}  <- plays an index of a search query. You find those indexes after you search for something or open a playlist or a channel with 'cd'. Nostop argument makes it so the playback will continue after the first song/video ends. Shuffle will shuffle the videos and works only with {nostop}")
    print("  play list <name_of_list> index<index> {shuffle}   <- plays from offline playlist <name_of_list> starting on index <index> and there's an option to shuffle. Notice no space between index and <index>")
    print("  shuffle <index>  <- shuffles a YouTube playlist, a channel or an album, designed to be quick to type")

    print("")
    print("")

    print("Albums:")
    print("Albums are online playlists, channels or songs stored in a database, so you won't have to search for them when you want to listen to them.")
    print("  album  <- lists all the albums, also replaces search results with them, so you can use 'cd', 'play index', or 'shuffle' on them.")
    print("  addbum <index> <- add the element <index> from search results as an album.")


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