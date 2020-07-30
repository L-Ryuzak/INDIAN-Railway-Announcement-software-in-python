import os
import pandas as pd
from pydub import AudioSegment  #using audiosegment we can do all kind of stuffs with audio  pyaudio only needs ffmpeg that we have already instlled
from pydub.playback import play
from gtts import gTTS
from playsound import playsound

def textToSpeech(text,filename):    #function which will take text as input and convert it into mp3 format saving it as filename.mp3
    sampletext = str(text)
    language = 'hi'
    obj = gTTS(text=sampletext, lang=language, slow=False)
    obj.save(filename)

def mergeAudios(audios):  #this functon will return audio object which we are merging
    concatenate = AudioSegment.empty()
    for audio in audios:
        concatenate += AudioSegment.from_mp3(audio)
    return concatenate


def generate_fragments():
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 88000   #1 generating ("krupiya dhyan dijiye")
    finish = 90300
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi_file.mp3",format="mp3")

    start = 91000   #3 generating ("se chalkar")
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi_file.mp3",format="mp3")

    start = 94000  #5 genrating("ke raste")
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi_file.mp3",format="mp3")

    start = 96000  #7 generating("ko jane wali gaddi sankhhya")
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi_file.mp3",format="mp3")

    start = 105500  #9 generating("kuch hi samay me platform sankhya")
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi_file.mp3",format="mp3")

    start = 109000   #11 generating("par aarhi he")
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi_file.mp3",format="mp3")


def generateAnnouncement(filename):    #takes .csv filename
    df = pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():  #pandas dataframe function which iterate through all rows in index file
                                     # now lets generate 2 mp3 which will be city name from which our train is departing  or from city
        textToSpeech(item['from'],'2_hindi_file.mp3')
                                     # generating via city mp3
        textToSpeech(item['via'],'4_hindi_file.mp3')
                                      # generating to city
        textToSpeech(item['to'],'6_hindi_file.mp3')
                                      # generating the train number and name mp3
        textToSpeech(item['train_no'] + " " + item['train_name'],'8_hindi_file.mp3')
                                      # generating platform number mp3
        textToSpeech(item['platform'],'10_hindi_file.mp3')

        audios = [f"{i}_hindi_file.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
 
        announcement.export(f"final_file_{index + 1}.mp3",format="mp3")


if __name__ == "__main__":
    print("Generating the fragments of audios.....")
    generate_fragments()
    print("Now generating announcement")
    generateAnnouncement("added_data_file.xlsx")
    df = pd.read_excel("added_data_file.xlsx")
    for index,item in df.iterrows():
        song = AudioSegment.from_mp3(f"final_file_{index + 1}.mp3")
        play(song)
    




