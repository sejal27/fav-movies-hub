import media #contains the definition of the class Movie
import webpage_builder #contains function to create and open the html file that displays all the movies and opens youtube trailer. 

#Create an instance of the Movie class for each new movie and assign title, storyline, wikipedia poster url, and youtube trailer url respectively.

belle = media.Movie("Belle",
                       "The illegitimate daughter of a navy admiral is trained and brought up by her aristocratic uncle and his wife.",
                       "https://upload.wikimedia.org/wikipedia/en/0/0f/Belle_poster.jpg",
                       "https://www.youtube.com/watch?v=9Qx90wdRD2I")
    

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

avengers = media.Movie("Avengers",
                       "Superheroes unite to save the world from an alien villian.",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

the_great_debaters = media.Movie("The Great Debaters",
                                 """A black professor at Wiley College,
                                 motivates his black students to form the first ever debate team.""",
                                 "https://upload.wikimedia.org/wikipedia/en/f/f5/Great_debaters_post.jpg",
                                 "https: // www.youtube.com / watch?v = wKSu5PlE3Ms)")

north_country = media.Movie("North Country",
                            "A fictionalized account of one of America's most groundbreaking sexual harassment lawsuit.",
                            "https://upload.wikimedia.org/wikipedia/en/0/0d/NorthCountryPoster.jpg",
                            "https://www.youtube.com/watch?v=jXkVQm0QPyY")

the_hunger_games = media.Movie("The Hunger Games",
                               """Katniss volunteers to replace her sister in a tournament,
                                where the participants must kill their counterparts.""",
                               "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                               "https://www.youtube.com/watch?v=4S9a5V9ODuY")

thor = media.Movie("Thor",
                   "Thor is exiled by his father Odin, the King of Asgard, to the Earth to live among mortals.",
                   "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

#Add all the instances in a list
movies = [the_great_debaters,belle,north_country,avatar,avengers,the_hunger_games,thor]

#open html page that displays movies in the list
webpage_builder.open_movies_page(movies)
