PREFERED_ENCODING = "utf-8"

def read_songs(file_name):
    try:
        with open(file_name, "r", encoding=PREFERED_ENCODING) as file:
            songs = file.readlines()
        songs_list = [song.strip() for song in songs]
        return songs_list
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file {file_name}: {e}")
        return []


def save_sorted_songs(songs, file_name):
    try:
        sorted_songs = sorted(songs)
        with open(file_name, "w", encoding=PREFERED_ENCODING) as file:
            for song in sorted_songs:
                file.write(song + "\n")
    except Exception as e:
        print(f"An error occurred while writing to the file {file_name}: {e}")


def main():
    input_file = "songs.txt"
    output_file = "sorted_songs.txt"

    songs = read_songs(input_file)
    if not songs:
        print("No songs were read.")
        return
    save_sorted_songs(songs, output_file)



if __name__ == "__main__":
    main()
