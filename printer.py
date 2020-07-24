import colorama
import os
import platform

def print_search_results(search_res):
    colorama.init()
    for res in search_res:
        title = f"{colorama.Fore.BLUE} {str(res['id'])}"
        if res['type'] != 'TV':
            title = f"{title} {colorama.Fore.CYAN} {res['type']}"
            if int(res['episodes_length'])>50 and res['type'] != 'Movie':
                title = f"{title}(Movie)"
        title = f"{title} {colorama.Fore.GREEN} {res['title']} {colorama.Style.RESET_ALL}"
        print(title)
        print(f"year: {res['date']}\t Episodes: {res['episodes_count']}\t Episode length: {res['episodes_length']} minutes")

def open_new_terminal():
    os_sys = platform.system()
    os_temrinal = ""
    if os_sys == "Linux":
        os_temrinal = "xterm" #Linux
    if os_sys == "Darwin":
        os_temrinal = "open -a Terminal -n" #macOS
    if os_sys == "Windows":
        os_temrinal = "start" #Windows
    return os_temrinal

def print_selected_anime_episodes(selected_anime):
    colorama.init()
    title = f"{colorama.Fore.BLUE} {str(selected_anime['id'])}"
    if selected_anime['type'] != 'TV':
        title = f"{title} {colorama.Fore.CYAN} {selected_anime['type']}"
        if int(selected_anime['episodes_length']) > 50 and selected_anime['type'] != 'Movie':
            title = f"{title}(Movie)"
    title = f"{title} {colorama.Fore.GREEN} {selected_anime['title']} {colorama.Style.RESET_ALL}"
    print(title)
    print(f"year: {selected_anime['date']}\t Episodes: {selected_anime['episodes_count']}\t Episode length: {selected_anime['episodes_length']} minutes")
    print("Episodes: ")
    has_vvvvid_link = False
    for episode in selected_anime['episodes']:
        print(episode['link'])
        if "vvvvid.it" in episode['link']:
            has_vvvvid_link = True
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "VVVVID"
            abs_file_path = os.path.join(script_dir, rel_path)
            f = open("downloads_list.txt", "a")
            f.write(episode['link'] + "\n")
            f.close()
    if has_vvvvid_link:
        vvvvid_download = input("\nThere are links from VVVVID, do you want to download them using \"CoffeeStraw/VVVVID-Downloader\"? yes/no: ")
        if vvvvid_download.lower() == "y" or vvvvid_download.lower() ==  "yes":
            #os.system(open_new_terminal())  -> It starts a new teminal but the new command is written on the same terminal
            if not os.path.isfile(abs_file_path+"/main.py"):
                print("Please, install CoffeeStraw/VVVVID-Downloader")
            else:
                os.system("python3 "+abs_file_path+"/main.py")
        os.remove("downloads_list.txt")