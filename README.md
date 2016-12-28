# The Hub of my Forever Favorite Movies!
This code launches a webpage that displays some of my forever favorite movies, along with a short storyline of each movie. You can click on the movie to watch the trailer. 

# Author
Sejal Parikh

# How to Use
1. Download all the files in the same folder.
2. Open movie_trailer_hub.py either by using command prompt, IDLE, or any other Python IDE (such as PyCharm).
3. If you want to add more movies, create instances of your movie using class Movie. See in media.py file for the class definition.
4. Append your new instance of the class Movie to the list 'movie'.
5. Run the movie_trailer_hub.py file.

# Source Files
1. media.py : Contains class definition and constructor function.
2. movie_trailer_hub.py : Contains instances of class Movie and passes them as a list to the function that opens the webpage.
3. webpage_builder.py : Contains function open_movies_page that takes in the list of movies (instances of the class Movie) and dynamically creates an html page(movie_trailer_hug.html) in the same folder. This page displays all the movies in tile format with movie poster, title, and storyline. Clicking on any movie tile loads its youtube trailer.
4. movie_trailer_hub.html : A sample output html page.

# Troubleshooting
If the file does not open in your default webbrowser, try to open the html file in Firefox or Chrome. Contact sejalrparikh@gmail.com for any other issues.

# License
GNU General Public License v3
