import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    """Return the average rating rounded to one decimal."""
    total_rating = sum(movie["rating"] for movie in movies)
    return round(total_rating / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Return oldest, newest and rounded-up average ages."""
    ages = [current_year - movie["year"] for movie in movies]
    return max(ages), min(ages), math.ceil(sum(ages) / len(ages))


def duration_in_hours(minutes):
    """Format a duration in minutes as hours and remaining minutes."""
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


def rating_tier(rating):
    """Return the category corresponding to the movie rating."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Return the release period label for the given year."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


def print_non_comedy_movies(movies):
    """Print titles of movies that do not belong to the comedy genre."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def print_first_masterpiece(movies):
    """Print the first movie rated above 9.0 or a message if none is found."""
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > 9.0:
            print(movie["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Count movies with a duration strictly greater than the threshold."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    """Capitalize the first letter of each word and join words with spaces."""
    words = title.split()
    normalized_words = []
    for word in words:
        normalized_words.append(word[0].upper() + word[1:])
    return " ".join(normalized_words)


def make_slug(title):
    """Convert a normalized title to a lowercase slug separated by hyphens."""
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    """Format a movie with its normalized title, duration and sorted genres."""
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


def titles_sorted_by_rating(movies):
    """Return movie titles sorted by rating in descending order."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Return the top n movies as (title, rating) tuples."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    """Return the number of movies in each genre."""
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    """Return movie titles for each actor in catalog order."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            actor_titles = filmography.get(actor, [])
            actor_titles.append(movie["title"])
            filmography[actor] = actor_titles
    return filmography


def above_average_ratings(movies):
    """Return titles and ratings above the catalog's rounded average rating."""
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average
    }


def main():
    print("Фильмы без жанра comedy:")
    print_non_comedy_movies(movies)
    print("\nПервый фильм с рейтингом выше 9.0:")
    print_first_masterpiece(movies)
    print(f"\nФильмов длиннее 120 минут: {count_long_movies(movies)}")

    print(normalize_title("silent hours"))
    print(make_slug("Silent Hours"))
    print(format_report_line(movies[7]))
    print(top_n_by_rating(movies, 3))
    print(count_by_genre(movies))
    print(actor_filmography(movies))
    print(above_average_ratings(movies))


if __name__ == "__main__":
    main()
