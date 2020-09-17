from pytube import YouTube

# YouTube('https://youtu.be/9bZkp7q19f0'). streams.first().download()

# Download path
SAVE_PATH = 'Download/'

# Throw an excemption if some errors occurs
try:
	url_link = 'http://youtube.com/watch?v=9bZkp7q19f0'
	yt = YouTube(url_link)
	# download 1st stream format
	stream = yt.streams.first()
	# download video 📹
	stream.download(SAVE_PATH)
	#yt.streams.filter(progressive=True).all()
	
	# if an error occurs
except:
		print("Failed To Establish Download, Some Error Occurred!")
		
		# if no error occurs
else:
	print("Successfully Downloaded")
