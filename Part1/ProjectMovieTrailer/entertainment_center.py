import media
import fresh_tomatoes

# initializing six movies using the Movie constructor
poh = media.Movie("Pursuit of Happiness", "A real story about pusrsuing your dreams",
                  "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                  "https://www.youtube.com/watch?v=89Kq8SDyvfg")


interstellar = media.Movie("Interstellar", "A mind-boggling movie about space and time",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")


pretty_woman = media.Movie("Pretty Woman", "A romantic movie",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/Pretty_woman_movie.jpg",
                           "https://www.youtube.com/watch?v=Wzii8IuL8lk")


thats_my_boy = media.Movie("That's my boy", "A very funny movie",
                           "https://upload.wikimedia.org/wikipedia/en/1/11/That%27s_My_Boy_poster.jpg",
                           "https://www.youtube.com/watch?v=fPV2L2CGWdQ")


fifty_first_dates = media.Movie("Fifty first dates", "A great romantic-comedy movie",
                                "https://upload.wikimedia.org/wikipedia/en/9/9d/50FirstDates.jpg",
                                "https://www.youtube.com/watch?v=ErjP5xMTc8I")


jumanji = media.Movie("Jumanji", "A movie about a game",
                             "https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png",
                             "https://www.youtube.com/watch?v=2QKg5SZ_35I")

# making a list of all the movies
movies = [poh, interstellar, pretty_woman, thats_my_boy, fifty_first_dates, jumanji]


# calling the function to open the web page
fresh_tomatoes.open_movies_page(movies)
