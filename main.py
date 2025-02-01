#import libraries
from pypdf import PdfReader
import pyttsx3
from tkinter.filedialog import *

#select book or pdf text from files
book = askopenfilename()

reader = PdfReader(book)
#print page number to terminal
print(len(reader.pages))

#loop through each page and read aloud
for i in range(0,len(reader.pages)-1):
    engine = pyttsx3.init()
    engine.say('I will speak this text')
    engine.say('page number ' + str(i))
    page = reader.pages[i]
    engine.say(page.extract_text())
    engine.runAndWait()    
