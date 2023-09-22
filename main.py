import PyPDF2
import pyttsx3

path = open('hamlet.pdf', 'rb')
speaker = pyttsx3.init()
pdfreader = PyPDF2.PdfReader(path)

for numbP in range(len(pdfreader.pages)):
    text = pdfreader.pages[numbP].extract_text()
    print(text.capitalize())

speaker.say(text.strip())
speaker.runAndWait()
