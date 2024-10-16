import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
        )
''')

def list_video():
    cursor.execute("SELECT * FROM videos") # we will get a tuple in result
    for row in cursor.fetchall(): 
        print(row)

def add_video(name ,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)",(name, time))
    conn.commit()

def update_video(vidoeId, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, vidoeId))
    conn.commit()

def delete_video(videoId):
    cursor.execute("DELETE FROM videos WHERE id = ?", (videoId))
    conn.commit()

def main():
    while True:
        print("\n Youtube video manager app with DB ")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update video details")
        print("4. Delete video")
        print("5. Exit the app")

        choice = input("Enter your choice : ")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter video name : ")
            time = input("Enter video time : ")
            add_video(name, time)
        elif choice == '3':
            videoId = input("Enter the Id of video to be updated : ")
            name = input("Enter video name : ")
            time = input("Enter video time : ")
            update_video(videoId, name , time)
        elif choice == '4':
            videoId = input("Enter the Id of video to be deleted : ")
            delete_video(videoId)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()