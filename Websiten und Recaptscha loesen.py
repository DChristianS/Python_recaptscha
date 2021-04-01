# Recaptscha Lösen
# 01. Seite mit ReCaptcha aufrufen
# 02. Frame mit ReCaptcha suchen
# 03. Warten
# 04. Checkbox bestätigen
# 05. Warten
# 06. Audio-Challenge auswählen
# 07. Warten
# 08. Audio Challenge anhören
# 09. Link mit Audio-Challenge finden und herunterladen
# 10. Audio-Challenge mit Google-Voice-Recognition in Text umwandeln
# 11. Text eingeben und bestätigen

# pip install selenium  (Browser)
# ffmpeg installieren und in Umgebungsvariablen einbinden
# pip install pydub
# pip install webdriver-manager
# pip install SpeechRecognition

import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pydub
import urllib
import speech_recognition

data_path = "Pfad/zur/Python/Datei"
browser = webdriver.Chrome("chromedriver.exe")              #Instanz zum ChromeWebBrowser erzeugen
browser.get("https://www.google.com/recaptcha/api2/demo")

# Checkbox 'Ich bin kein Roboter' suchen
frames = browser.find_elements_by_tag_name("iframe")
browser.switch_to.frame(frames[0])
time.sleep(random.randint(2,4))
browser.find_element_by_class_name("recaptcha-checkbox-border").click()

# Audiochallenge anfordern
browser.switch_to.default_content()
frames = browser.find_element_by_xpath("/html/body/div[2]/div[4]").find_element_by_tag_name("iframe")
browser.switch_to.frame(frames[0])
time.sleep(random.randint(2,4))
browser.find_elements_by_id("recaptcha-audio-button").click()

# Audiochallenge anhören
browser. switch_to.default_content() 
frames = browser.find_elements_by_tag_name("iframe")
browser.switch_to.frame(frames[-1])
time.sleep(random.randint(2,4))
browser.find_element_by_xpath("/html/body/div/div/div[3]").click()

# Audiodatei Herunterladen
src = browser.find_elements_by_id("audio-source").get_attribute("src")
urllib.request.urlretrieve(src, data_path + "\\audio.mp3")
sound = pydub.AudioSegment.from_mp3(data_path + "\\audio.mp3").export(data_path + "\\audio.wav", format="wav" )
recognizer = speech_recognition.Recognizer()
google_audio = speech_recognition.AudioFile(data_path + "\\audio.wav")
with google_audio as source:
    audio = recognizer.record(source)
text = recognizer.recognize_google(audio, language='de-DE')
print("<Erkannter Text> : {}".format(text))

# Text Eintragen
inputfield = browser.find_elements_by_id("audio-response")
inputfield.send_keys(text.lower())
inputfield.send_keys(Keys.ENTER)
