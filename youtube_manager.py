import json
    
def load_data():
    try:
        with open('myvideo.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 

def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass


def main():
    videos=load_data()
    while True:
        print('Youtube manager |choose an option')
        print('1. List all youtube videos')
        print('2. Add youtube video')
        print('3. Update youtube video details:')
        print('4. Delete the video')
        print('5. Exit the app')
        choice=input("Enter a number: ")
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
                
if __name__=='__main__':
    main()
    
            
                