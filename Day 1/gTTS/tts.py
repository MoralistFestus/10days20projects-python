#import gtts module
from gtts import gTTS
"""Module is imported in order to play converted audio """
import os
mytext = "Welcome to text to speech"
#Language 
language = "en" #English 
#Do some functions
myobj = gTTS(text=mytext, lang=language, slow=False)
#Save as mp3
myobj.save("welcome.mp3")
#play
os.system("mpg321 welcome.mp3")
