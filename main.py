import re
import pyttsx3
from PyPDF2 import PdfReader

def read_pdf():
  pdf = PdfReader('book.pdf')
  return ' '.join([re.sub(r'\s+', ' ', page.extract_text().strip()) for page in pdf.pages])

def save_audio(read_pdf):
  speaker.save_to_file(read_pdf, 'book.ogg')
  speaker.runAndWait()
  speaker.stop()

def speak(read_pdf):
  speaker.say(read_pdf)
  speaker.runAndWait()
  speaker.stop()

def change_voice(speaker, language, gender='VoiceGenderFemale'):
  for voice in speaker.getProperty('voices'):
    #print(voice.languages)
    #print(voice.gender)
    if language in voice.languages and gender == voice.gender:
      speaker.setProperty('voice', voice.id)
      return True
  raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

if __name__ == '__main__':
  stripped_text = read_pdf()
  #print(stripped_text)
  speaker = pyttsx3.init()
  english = b'\x02en-gb'
  deutsch = b'\x05de'
  change_voice(speaker, english, 'male')
  speaker.setProperty('rate', 160)
  speak(stripped_text)
  save_audio(stripped_text)
