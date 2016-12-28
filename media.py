import webbrowser #import webbrowser module to open the webpage.

"""This module contains definition of class Movie,
functions to inits the class, and open the official movie trailer."""

class Movie():
    """This class stores all the movies and related attributes and functions.

    Use this class to create an instance of a new movie.

    Attributes:
        VALID_RATINGS: Ratings given to the movie
        title: Title of the movie
        storyline: A short description of the movie explaining its storyline.
        poster_image_url: url of the box-art imagery or poster image sourced with permission
        trailer_youtube_url: Youtube link to the official movie trailer

    Functions:
        __init__: Takes title, storyline, poster_image_url, and trailer_youtube_url respectively as attributes and
                  Creates a new instance of the Movie.
        show_trailer: Opens the youtube trailer from the link given in trailer_youtube_url"""

    VALID_RATINGS = ["G", "PG", "PG-13"] #Class variable

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This function opens the youtube trailer from the link given in the trailer_youtube_url"""
        webbrowser.open(self.trailer_youtube_url)
    
