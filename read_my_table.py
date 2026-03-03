# read_spotify.py
# Reads all items from the DynamoDB Spotify table and prints them

import boto3

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Spotify"


def get_table():
    """Return a reference to the DynamoDB Spotify table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_song(song):
    title = song.get("Title", "Unknown Title")
    artist = song.get("Artist", "Unknown Artist")
    rating = song.get("Rating", "No rating")

    print(f"  Title  : {title}")
    print(f"  Artist : {artist}")
    print(f"  Rating : {rating}")
    print()


def print_all_songs():
    """Scan the entire Spotify table and print each item."""
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No songs found. Make sure your DynamoDB table has data.")
        return

    print(f"Found {len(items)} song(s):\n")
    for song in items:
        print_song(song)


def main():
    print("===== Reading from DynamoDB (Spotify) =====\n")
    print_all_songs()


if __name__ == "__main__":
    main()