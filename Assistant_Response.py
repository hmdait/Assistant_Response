import speech_recognition as sr
from gtts import gTTS
import os
import warnings
import datetime
import random
import calendar
import wikipedia

warnings.filterwarnings('ignore')


def RecordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("i'm listening :")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio)
        print('you said :{}'.format(data))
    except sr.RequestError as e:
        print('soory')
    except sr.UnknownValueError:
        print('google speech recognition could not undertand the audio')

    return data


def AssistantResponse(text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save('assistant_response1.wav')
    os.system('start assistant_response1.wav')


def WakeWord(text):
    Wake_Word = ['hello mary', 'okay mary']

    text = text.lower()
    for phrase in Wake_Word:
        if phrase in text:
            return True

    return False


def GetDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['january', 'February', 'March', 'april', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    ordinalNumbers = ['1st', '2d', '3th', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                      '14th', '15th', '16th', '17th', '18th',
                      '19th', '20th', '21st', '22d', '23th', '24th', '25th', '26th', '27th', '28th', '29th', '30th',
                      '31th']
    return 'today is ' + weekday + ' '' the ' + ordinalNumbers[dayNum - 1] + ',' + month_names[monthNum - 1] + ' sir.'


def Getting(text):
    GREETING_RESPONS = ['howdy', 'whats good', 'hello', 'hey there']
    GEETING_INPUT = ['he', 'hry', 'hola', 'wassup', 'hello']

    for word in text.split():
        if word.lower() in GEETING_INPUT:
            return random.choice(GREETING_RESPONS) + '.'

    return ''


def GetPerson(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]


while True:

    text = RecordAudio()
    response = ''

    if (WakeWord(text) == True):
        response = response + Getting(text)
        if ('date' in text):
            get_date = GetDate()
            response = response + '' + get_date

        if ('time' in text):
            now = datetime.datetime.now()
            Meridiem = ''

            if now.hour >= 12:
                Meridiem = 'p.m'
                hour = now.hour - 12
            else:
                Meridiem = 'a.m'
                hour = now.hour

            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

            response = response + ' ' + 'it is ' + str(hour) + ': ' + minute + ' ' + Meridiem + '.'

        if 'who is' in text:
            person = GetPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        if 'level 6' in text:
            response = 'confomation of level 6 '

        if 'level 5' in text:
            response = 'confomation level 5 '



        AssistantResponse(response)
