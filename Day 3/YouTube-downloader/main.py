from pytube import YouTube 

# Download path
SAVE_PATH = "Download/"

# url file
url_link = open('links_file.txt','r')

# iterate
for i in url_link: 
    try: 
        yt = YouTube(i) 
    except: 
        print("Connection Error")
        
     
    # downloading video
    try:
        d_video.download(SAVE_PATH) 
    except: 
        print("Some Error!") 
print('Task Completed!') 