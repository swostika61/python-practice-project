import sqlite3

con = sqlite3.connect("video_list.db")
cur = con.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS video_list(
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL, 
        time TEXT NOT NULL
    )
''')

def line_break(text):
    print('*'*70)
    print(text)
    print('*'*70)
    print('\n')

def list_all_videos():
    print('*'*70)
    cur.execute('SELECT * FROM video_list')
    print('VIDEO LIST: ')
    for video in cur.fetchall():
        print(video)
    print('*'*70)

def add_video():
    name = input('Enter a video name: ')
    time = input('Enter the video time: ')
    cur.execute("INSERT INTO video_list(name, time) VALUES(?, ?)", (name, time))
    con.commit()
    line_break('ADDED SUCCESSFULLY!!')

def update_video():
    list_all_videos()
    id = int(input('Enter video id to update: '))
    name = input('Enter new video name: ')
    time = input('Enter new video time: ')
    cur.execute('''
    UPDATE video_list
    SET name = ?, time = ?
    WHERE id = ?
    ''', (name, time, id))
    con.commit()
    line_break('UPDATED SUCCESSFULLY!!')

def delete_video():
    id = int(input('Enter video id to delete: '))
    cur.execute('''
        DELETE FROM video_list
        WHERE id = ?
    ''', (id,))
    con.commit()
    line_break('DELETED SUCCESSFULLY!!')

def main():
    while True:
        print('***Youtube manager | Choose an option***')
        print('1. List all youtube videos')
        print('2. Add youtube video')
        print('3. Update youtube video details')
        print('4. Delete the video')
        print('5. Exit the app')
        choice = input("Enter a number to choose the listed option: ")
        match choice:
            case '1':
                list_all_videos()
            case '2':
                add_video()
            case '3':
                update_video()
            case '4':
                delete_video()
            case '5':
                break
            case _:
                print("Invalid Choice!! \n")
    con.close()

if __name__ == "__main__":
    main()
