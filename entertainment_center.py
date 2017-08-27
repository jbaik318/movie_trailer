#This file contains each movie's title, summary, poster image, and trailer link.

import media
import fresh_tomatoes

'''
These instance variables are called for each movie.
After setting these instance variables into a single object
'''

#Iron Man Movie
iron = media.Movie("Iron Man",
					"""A billionaire industrialist and genius inventor, Tony Stark (Robert Downey Jr.), 
					is conducting weapons tests overseas, but terrorists kidnap him to force him to build a devastating weapon. 
					Instead, he builds an armored suit and upends his captors. Returning to America, 
					Stark refines the suit and uses it to combat crime and terrorism.""",
					"http://www.gstatic.com/tv/thumb/movieposters/170620/p170620_p_v8_ak.jpg",
					"https://www.youtube.com/watch?v=XWWd6p2JHKo")

#The Incredible Hulk Movie
hulk = media.Movie("The Incredieble Hulk",
					"""Scientist Bruce Banner (Edward Norton) desperately seeks a cure for the gamma radiation that contaminated his cells 
					and turned him into The Hulk. Cut off from his true love Betty Ross (Liv Tyler) and forced to hide from his nemesis, 
					Gen. Thunderbolt Ross (William Hurt), Banner soon comes face-to-face with a new threat: a supremely powerful enemy known 
					as The Abomination (Tim Roth).""",
					"http://www.gstatic.com/tv/thumb/movieposters/176337/p176337_p_v8_ah.jpg",
					"https://www.youtube.com/watch?v=xbqNb2PFKKA")

#Iron Man 2 Movie
iron2 = media.Movie("Iron Man 2",
						"""With the world now aware that he is Iron Man, billionaire inventor Tony Stark (Robert Downey Jr.) 
						faces pressure from all sides to share his technology with the military. He is reluctant to divulge the 
						secrets of his armored suit, fearing the information will fall into the wrong hands. With Pepper Potts 
						(Gwyneth Paltrow) and "Rhodey" Rhodes (Don Cheadle) by his side, Tony must forge new alliances and confront 
						a powerful new enemy.""",
						"http://t1.gstatic.com/images?q=tbn:ANd9GcTbUWVX-6eusHp85uW6cbtbwzrW5UtBXgpc2FkCQEJ_YUO574gO",
						"https://www.youtube.com/watch?v=oOzuBOefL8I")

#Thor Movie
thor = media.Movie("Thor",
				  """As the son of Odin (Anthony Hopkins), king of the Norse gods, Thor (Chris Hemsworth) will soon inherit the throne of 
				  Asgard from his aging father. However, on the day that he is to be crowned, Thor reacts with brutality when the gods' enemies, 
				  the Frost Giants, enter the palace in violation of their treaty. As punishment, Odin banishes Thor to Earth. While Loki 
				  (Tom Hiddleston), Thor's brother, plots mischief in Asgard, Thor, now stripped of his powers, faces his greatest threat.""",
				  "http://t0.gstatic.com/images?q=tbn:ANd9GcRSZN3c1Wj6s6Nz0DLOYTZY4GM27rt6zRDCdw_z_0ff8oAKTeXE",
				  "https://www.youtube.com/watch?v=JOddp-nlNvQ")

#Captain America Movie
captain = media.Movie("Captain America: The First Avenger",
					  """It is 1941 and the world is in the throes of war. Steve Rogers (Chris Evans) wants to do his part and join 
					  America's armed forces, but the military rejects him because of his small stature. Finally, Steve gets his chance 
					  when he is accepted into an experimental program that turns him into a supersoldier called Captain America. Joining 
					  forces with Bucky Barnes (Sebastian Stan) and Peggy Carter (Hayley Atwell), Captain America leads the fight against 
					  the Nazi-backed HYDRA organization.""",
					  "http://t3.gstatic.com/images?q=tbn:ANd9GcQxM9vgeSWLNfQ46gItm926mnual8QWSVyUTAy6HSefuJqeyFWs",
					  "https://www.youtube.com/watch?v=JerVrbLldXw")

#Avenger's Movie
avenger = media.Movie("Marvel's The Avengers",
					  """When Thor's evil brother, Loki (Tom Hiddleston), gains access to the unlimited power of the energy cube 
					  called the Tesseract, Nick Fury (Samuel L. Jackson), director of S.H.I.E.L.D., initiates a superhero recruitment 
					  effort to defeat the unprecedented threat to Earth. Joining Fury's "dream team" are Iron Man (Robert Downey Jr.), 
					  Captain America (Chris Evans), the Hulk (Mark Ruffalo), Thor (Chris Hemsworth), the Black Widow (Scarlett Johansson)
					   and Hawkeye (Jeremy Renner).""",
					  "http://t1.gstatic.com/images?q=tbn:ANd9GcTp0qlAoWcOOswIkL_qpjYzJqCCDmWXiBzCXiqbE43Obo8c0Z-s",
					  "https://www.youtube.com/watch?v=eOrNdBpGMv8")



#Each movie object is set into an array that can be iterated.
movies = [iron,hulk,iron2,thor,captain,avenger]

'''
The array of movie objects are iterated by a function called open_movies_pages 
located in the fresh_tomateoes file.
'''
fresh_tomatoes.open_movies_page(movies)

