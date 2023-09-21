import json, os, requests
folder_path = "C:\\Users\\yzn-\\Desktop\\YacineChatt"

total_messages = 0
total_files = 0
total_vod_length = 0
average_viewers = 0
vod_viewers = 0 

def count_messages_in_file(folder_path):
    with open(folder_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    messages = data.get("comments", [])
    return len(messages)

def count_vod_length(folder_path):
    with open(folder_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    vod_object = data.get("video", [])
    vod_length = vod_object.get("length", [])
    return (vod_length/60)

def total_viewcount_session(folder_path):
    with open(folder_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    vod_object = data.get("video", [])
    vod_viewers = vod_object.get("viewCount", [])
    return(vod_viewers)

def get_average_viewers():
    url = "https://twitchtracker.com/api/channels/summary/Yacine"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        average_viewers = data.get("avg_viewers", 0)
        return average_viewers
    else:
        print(f"Oops! Something went wrong. Status code: {response.status_code}")
        return 0

if __name__ == "__main__":
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            message_count = count_messages_in_file(file_path)
            vod_count = count_vod_length(file_path)
            vod_viewers_count = total_viewcount_session(file_path)
            total_messages += message_count
            total_files += 1
            total_vod_length += vod_count
            vod_viewers += vod_viewers_count
average_viewers = get_average_viewers()
print(f"Totalt får denna twitchare ungefär {round(total_messages/(total_vod_length))} meddelanden per minut. Twitcharen har en average viewer på {average_viewers} och i genomsnitt {round(vod_viewers/total_files)} som kollar per VOD, totalt {total_files} stycken!")