# This AI Speaker code can recognize your voice and what you say via microphone
# When you say something, this code sends a message to microprocessor-board based on serial communication(UART)
# This AI Speaker tell you weather, Exchange rate, time
# This AI speaker allows your voice to turn on and off LEDs connected to hardware .
import multiprocessing
import threading
import winsound
import time, os
import math
import speech_recognition as sr
import requests
import json
from bs4 import BeautifulSoup
import urllib.request
from gtts import gTTS
from playsound import playsound
import serial
##############################UART
uart_temp = 0
py_serial = serial.Serial(
    
    # Window
    port='COM5',
    
    # 보드 레이트 (통신 속도)
    baudrate=9600,
)
number=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h']
#number=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
################################## Exchange_rate in real time (API)
url_usd = "https://finance.naver.com/marketindex/"
res_usd = urllib.request.urlopen(url_usd).read()
soup_usd = BeautifulSoup(res_usd, "html.parser")
usd = soup_usd.find('select',id="select_to", class_="selectbox-source")
exchange_rate = {}
for opt in usd.find_all('option'):
    exchange_rate[opt.text[-3:]]=float(opt['value'])
us_dollar=int((exchange_rate)['USD'])
jp_yen=int((exchange_rate['JPY'])*100)
##################################

################################## Weather in real time(API)
city = "Tokyo" #Weather
apikey ="ec7929ada1089877731a831f01117891"
lang ="en"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&{lang}&units=metric"
result = requests.get(api)
data = json.loads(result.text)
##################################
exit_program = False
def main(): #Speaker main function
    
    def sendData(x):
        x = x.encode('utf-8')
        py_serial.write(x)

    def listen(recognizer, audio):
        try:
            text = recognizer.recognize_google(audio, language='en')
            print('[Human]'+text)
            answer(text)
            sendData(number[1])
            print(number[1])
        except sr.UnknownValueError:
            print('Recognition Failed')
            sendData(number[2])
            print(number[2])
        except sr.RequestError as e:
            print('Request Failed:{0}'.format(e))
            sendData(number[3])
            print(number[3])

    def answer(input_text):
        answer_text=''
        if 'hello' in input_text:
            if 6<=time.localtime().tm_hour < 12: 
                answer_text='Good Morning Sir'
                speak(answer_text)
                sendData(number[4])
                print(number[4])
            elif 12<=time.localtime().tm_hour < 18:
                answer_text='Good Afternoon Sir'
                speak(answer_text)
                sendData(number[5])
                print(number[5])
            elif 18<= time.localtime().tm_hour < 24:
                answer_text='Good evening Sir'
                speak(answer_text)
                sendData(number[6])
                print(number[6])
            else:
                answer_text="Sir, It would be better for you to go to bed"
                speak(answer_text)
                sendData(number[7])
                print(number[7])
    
        elif 'time' in input_text:
            answer_text =  "Time now is"+" "+str(time.localtime().tm_hour)+" "+str(time.localtime().tm_min)
            speak(answer_text)
            sendData(number[8])
            print(number[8])

        elif 'weather' in input_text:
            sendData(number[9])
            print(number[9])
            answer_text = "The weather of"+" "+data["name"]+" "+"now"
            speak(answer_text)
            answer_text = "Weather is"+" "+data["weather"][0]["description"]
            speak(answer_text)
            answer_text = "Temperature is"+" "+str(data["main"]["temp"])+" "+"now"
            speak(answer_text)

        elif 'exchange rate' in input_text:
            sendData(number[10])
            print(number[10])
            answer_text=str(us_dollar)+"won"+" "+" per 1 dollar"
            speak(answer_text)
            answer_text=str(jp_yen)+"won"+" "+" per 100 yen"
            speak(answer_text)

        elif 'on' in input_text:
            sendData(number[11])
            print(number[11])
            answer_text=" Yes sir Turn on the light"
            speak(answer_text)
        
        elif 'off' in input_text:
            sendData(number[12])
            print(number[12])
            answer_text=" Yes sir Turn off the light"
            speak(answer_text)
            
            
        elif 'out' in input_text:
            sendData(number[13])
            print(number[13])
            answer_text= 'See you next time'
            speak(answer_text)
            stop_listening(wait_for_stop=False)
            global exit_program
            exit_program = True 

        else:
            sendData(number[14])
            print(number[14])
            answer_text= 'Could you repeat that?'
            speak(answer_text)

    def speak(text):
        print('[Artificial Intelligence]'+text)
        file_name = 'voice.mp3'
        tts=gTTS(text=text,lang='en')
        tts.save(file_name)
        playsound(file_name)
        if os.path.exists(file_name):
            os.remove(file_name)
      
    r = sr.Recognizer()
    m = sr.Microphone()

    speak('May I help you?')
    sendData(number[15])
    print(number[15])

    stop_listening = r.listen_in_background(m, listen)
    while not exit_program:
        time.sleep(0.1)
if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
    print("speaker_end")


    
