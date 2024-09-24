import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        return json.dump(videos,file)
    
def list_all_videos(videos):
    print('\n')
    print('*'*70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    
    print('\n')
    print('*'*70)

def add_video(videos):
    name = input("Enter the name: ")
    time = input("Enter the time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    load_data(videos)
    index = int(input("Enter the number of video to be updated"))
    if 1<= index <= len(videos):
        name = print('Enter the new video name')
        time = print('Enter the duration of new video')
        videos[index-1]= {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")
    
    
def delete_video(videos):
    load_data(videos)
    index =int(input("Enter the video index to be deleted"))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    
    else:
        print("Wrong index selected")

def main():
    videos=load_data()

    while True:
        print('\n')
        print('Welcome to Youtube Manager | Enter a choice ')
        print('1. List all Youtube videos')
        print('2. Add a youtube video')
        print('3. Update the video details')
        print('4. Delete a  video')
        print('5. Exit the app\n')
        
        choice = input('Enter your choice')
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
            
if __name__ == "main":
    main()