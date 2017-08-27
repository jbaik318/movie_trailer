#This file is the constructor in which all information is stored per movie. 

class Movie ():
	def __init__(self, movie_title,movie_summary, poster_image_url, trailer_youtube_url):
		self.title = movie_title
		self.summary =  movie_summary
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

