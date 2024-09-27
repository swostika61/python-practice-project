import json

data_file_name='myvideo.txt'

def line_break(text):
    print('*'*70)
    print(text)
    print('*'*70)
    print('\n')

def load_data():
    try:
        with open(data_file_name,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_video_data(videos):
    with open(data_file_name,'w') as file:
        return json.dump(videos,file)

def list_all_videos(videos):
    print('*'*70)
    for index, video in enumerate(videos,start=1):
        print(f'{index}. {video['name']}, Duration:{video['time']} ')
    print('*'*70)

def add_video(videos):
    name= input("enter the name of the video:")
    time=input("enter the time of the video:")
    videos.append({'name':name,'time':time})
    save_video_data(videos)
    line_break('ADDED SUCCESSFULLY!!')

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter a video number to update: "))
    if 1<=index<=len(videos):
        name=input("enter new video name: ")
        time=input("enter the new duration: ")
        videos[index-1]={"name":name,"time":time}
        save_video_data(videos)
        line_break("UPDATED SUCCESSFULLY!!")
    else:
        line_break('INVALID SELECTION!!')

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter a video number to delete: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_video_data(videos)
        line_break("DELETED SUCCESSFULLY!!")
    else:
        line_break("INVALID SELECTION!!")

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
                print("Invalid Choice!! \n")
                
if __name__=='__main__':
    main()
    
            
                