import csv

NAME = "Name"
GENRE = "Genre"
DEVELOPER = "Developer"
ESRB_RATING = "ESRB Rating"
PREFERED_ENCODING = "utf-8"
FILE_NAME = "video_games.csv"


def write_video_games(file_name, video_games, fieldnames):
    try:
        with open(file_name, mode="w", encoding=PREFERED_ENCODING, newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(video_games)
    except IOError as e:
        print(f"An IO error occurred when writing the file {file_name}: {e}")
    except Exception as e:
        print(f"An error occurred when writing the file {file_name}: {e}")


def enter_video_games():
    video_games = []
    while True:
        try:
            name = input("Video game name: ")
            genre = input("Video game genre: ")
            developer = input("Video game developer: ")
            esrb_rating = input("Video game ESRB rating: ")

            video_games.append(
                {
                    NAME: name,
                    GENRE: genre,
                    DEVELOPER: developer,
                    ESRB_RATING: esrb_rating,
                }
            )

            continue_adding = input("Do you want to add another game? (y/n): ")
            if continue_adding.strip().lower() != "y":
                break
        except Exception as e:
            print(f"An error occurred when entering video game details: {e}")
    return video_games


def main():
    try:
        video_games = enter_video_games()
        if video_games:
            fieldnames = [NAME, GENRE, DEVELOPER, ESRB_RATING]
            write_video_games(FILE_NAME, video_games, fieldnames)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
