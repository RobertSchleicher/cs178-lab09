# read_movies.py
# Reads a movie from the DynamoDB Movies table by title
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Attr

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Movies"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_movie(movie):
    title = movie.get("Title", "Unknown Title")
    year = movie.get("Year", "Unknown Year")
    ratings = movie.get("Ratings", "No ratings")
    director = movie.get("Director", "Unknown Director")
    genre = movie.get("Genre", "Unknown Genre")

    print(f"  Title  : {title}")
    print(f"  Year   : {year}")
    print(f"  Ratings: {ratings}")
    print(f" Director : {director}")
    print(f" Genre : {genre}")
    print()


def get_movie_by_title():
    """Prompt the user for a movie title and search the DynamoDB table."""
    table = get_table()
    title = input("Enter the movie title: ").strip()

    # scan() with a FilterExpression to match the title
    response = table.scan(
        FilterExpression=Attr("Title").eq(title)
    )

    movies = response.get("Items", [])

    if movies:
        print(f"\nMovie(s) found with title '{title}':\n")
        for movie in movies:
            print_movie(movie)
    else:
        print(f"\nNo movie found with title '{title}'")


def main():
    print("===== Reading from DynamoDB =====\n")
    get_movie_by_title()  # call the prompt function


if __name__ == "__main__":
    main()
