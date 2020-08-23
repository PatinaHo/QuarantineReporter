# import speech_recognition as sr
# import time
# import os
# import sys
# import pyaudio
# import wave # 這是讀聲音檔的，可以不需要
# from pyaudio import PyAudio,paInt16
# import numpy as np

# #import parselmouth
# #from gpiozero import LED
# import time
# from datetime import datetime
# from gtts import gTTS
# from pygame import mixer
# import tempfile
# from gpiozero import LED
# from time import sleep
# import json
# from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
# import boto3

# # Infos for AWS IOT and file and others
# framerate=44100
# NUM_SAMPLES=512
# channels=1
# sampwidth=2
# TIME=2
# ACCESS_KEY = "ASIARCFG44K5KBF75PUY"
# SECRET_KEY = "gTFCKC2kMnsfHR5NPE3/M9S1zrU2LHTU2PMwpDc6"
# SESSION_TOKEN = "FwoGZXIvYXdzENn//////////wEaDF3VwEk9IUgaOQcQGCLKAfXbRFOaIdf3sKpztNGI780bIVrdej87jfC7A0DiXb8RWAdPYnQefjdLxEtGKc2TmDNeefVE2klQCNeJG4JiABP7qvzxGdr1SqwLhhJgC2FsbQz85BtJ65lZRg2s7lhzMhw1CpoaqWYdNVdtyt2pyLKxP9jnIXLQJ+7IIdwBu+tMxNw8395yRfo4VWH7t8kW5dgY3b1dLZrP3VzJYQ2ptwXFiycJ707066IkbFSUslBd1eLuWBYUxFdoc1pSTfaqF4595RFyOezve+0ojpDP9gUyLb7PdTF7hllUwFeVX5huSXS8UTg3gD074GP1yyRQs1E/bwvhlgcc5u36h5NVKQ=="
# host = "a1xqahltracscx-ats.iot.us-east-1.amazonaws.com"
# rootCAPath = "/home/pi/Desktop/deviceSDK/certs/AmazonRootCA1.pem"
# certificatePath = "/home/pi/Desktop/deviceSDK/certs/ba57b2be81-certificate.pem.crt"
# privateKeyPath = "/home/pi/Desktop/deviceSDK/certs/ba57b2be81-private.pem.key"
# port = 443
# clientId = "MyThing"
# publish_topic = "iot/topic"
# subscribe_topic = "iot/result"
# BUCKET_NAME = "team10-hackathon"

# def speak(sentence, lang):
#     with tempfile.NamedTemporaryFile(delete=False) as fp:
#         print(sentence)
#         tts=gTTS(text=sentence, lang=lang)
#         tts.save('{}.mp3'.format(fp.name))
#         mixer.init()
#         mixer.music.load('{}.mp3'.format(fp.name))
#         mixer.music.play(1)

# def save_wave_file(filename,data):
#     '''save the date to the wavfile'''
#     wf=wave.open(filename,'wb')
#     wf.setnchannels(channels)#聲道
#     wf.setsampwidth(sampwidth)#取樣位元組 1 or 2
#     wf.setframerate(framerate)#取樣頻率 8000 or 16000
#     wf.writeframes(b"".join(data))#https://stackoverflow.com/questions/32071536/typeerror-sequence-item-0-expected-str-instance-bytes-found
#     wf.close()

# def my_record(name):
#     pa=PyAudio()
#     stream=pa.open(format = paInt16,channels=1,
#                    rate=framerate,input=True,
#                    frames_per_buffer=NUM_SAMPLES)
#     my_buf=[]
#     count=0
#     red = LED(2)
#     red.off()
#     while count<TIME*133:#控制錄音時間
#         string_audio_data = stream.read(NUM_SAMPLES)#一次性錄音取樣位元組大小
#         my_buf.append(string_audio_data)
#         count +=1
#         print('.')
#     sleep(0.5)
#     red.on()
#     save_wave_file(name+'.wav',my_buf)
#     stream.close()


# # Custom MQTT message callback
# def customCallback(client, userdata, message):
#     print("Receive message:", message.payload.decode("utf-8"))
#     result_payload = message.payload.decode("utf-8")
#     if result_payload == "Danger":
#         speak("您有罹患COVID-19的可能性，請立即通報相關單位!", 'zh-tw')
#     else:
#         speak("您的健康狀況良好!", 'zh-tw')
#     return



def raspberryPi_starts():
    print("raspberryPi begins.")
    
    # condition = dict()
    # while(True):

    #     speak("體溫", 'zh-tw')
    #     sleep(1)
    #     print('Start!  '+ "體溫")
    #     my_record("體溫")
    #     recognizor = sr.Recognizer()
    #     intro = sr.AudioFile('{}.wav'.format("體溫"))
        
    #     with intro as source:

    #         try:
    #             audio = recognizor.record(source, offset = 0.0, duration = 3.0) 
    #             google_recognizor = recognizor.recognize_google(audio, language = "zh-tw", show_all = True)
            
    #             subtitle = google_recognizor["alternative"][0]["transcript"]
    #             print(subtitle)
    #         except:
    #             speak("數據不合理 請重複", 'zh-tw', )
    #             sleep(2)
    #             continue
            
            
    #         if subtitle == "":
    #             speak("數據不合理 請重複", 'zh-tw')
    #             sleep(2)
    #             continue
            
            
    #         subtitle = subtitle.replace("度","")
            
    #         try:
    #             if(32.0<=float(subtitle) and float(subtitle)<=45.0):
    #                 break
    #             else:
    #                 speak("數據不合理 請重複", 'zh-tw')
    #                 sleep(2)
    #         except:
    #             speak("數據不合理 請重複", 'zh-tw')
    #             sleep(2)
    #             continue
        
    # condition["體溫"] = float(subtitle)
    # print('Over!')
        
    # os.system("rm {}.wav".format("體溫"))  
    
    
    # for each in ["呼吸困難", "疲勞狀況", "肌肉酸痛", "頭疼狀況", "喪失味覺與嗅覺", "咳嗽或喉嚨痛", "鼻塞或流鼻水", "噁心或嘔吐", "腹瀉"]:
        
    #     while(True):
        
        
    #         speak(each+"一到五分 請給分", 'zh-tw')
    #         print('Start!  '+ each)
    #         sleep(5)
    #         my_record(each)
            
    #         recognizor = sr.Recognizer()
    #         intro = sr.AudioFile('{}.wav'.format(each))
            
    #         with intro as source:

    #             try:
    #                 audio = recognizor.record(source, offset = 0.0, duration = 3.0) 
    #                 google_recognizor = recognizor.recognize_google(audio, language = "zh-tw", show_all = True)
                
    #                 subtitle = google_recognizor["alternative"][0]["transcript"]
    #                 print(subtitle)
    #             except:
    #                 speak("數據不合理 請重複", 'zh-tw')
    #                 sleep(2)
    #                 continue
                
                
    #             if subtitle == "":
    #                 speak("數據不合理 請重複", 'zh-tw')
    #                 sleep(2)
    #                 continue
                
    #             subtitle = subtitle.replace("分","")
    #             try:
    #                 if(subtitle=="兩"):
    #                     subtitle="2"
    #                     break
    #                 elif(1<=int(subtitle) and int(subtitle)<=5):
    #                     break
    #                 else:
    #                     speak("數據不合理 請重複", 'zh-tw')
    #                     sleep(2)
    #             except:
    #                 speak("數據不合理 請重複", 'zh-tw')
    #                 sleep(2)
    #                 continue
        
        
        
    #     condition[each] = int(subtitle)
        
    #     print('Over!')
        
    #     os.system("rm {}.wav".format(each))
        
        
        
    # print()
    # print()
    # print()
    
    # condition_list = list()
    # for each in condition:
    #     print(each)
    #     print(condition[each])
    #     condition_list.append(str(condition[each]))
    # condition_payload = "|".join(condition_list)
    
    # test_path = "test_data.txt"
    # file = open(test_path,"w")
    # file.write(condition_payload)
    # file.close()
    
    # curdatetime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    # speak("照相中 請對鏡頭微笑", 'zh-tw')
    # sleep(5)
    # os.system("raspistill -v -o " + curdatetime + ".jpg")
    
    # # Init AWSIoTMQTTClient
    # myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
    # myAWSIoTMQTTClient.configureEndpoint(host, port)
    # myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

    # # AWSIoTMQTTClient connection configuration
    # myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    # myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    # myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    # myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    # myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    # # Connect and subscribe to AWS IoT
    # myAWSIoTMQTTClient.connect()
    # myAWSIoTMQTTClient.subscribe(subscribe_topic, 1, customCallback)
    # sleep(2)

    # # Publish to the same topic in a loop forever
    # myAWSIoTMQTTClient.publish(publish_topic, condition_payload, 1)
    # print('Published topic %s: %s\n' % (publish_topic, condition_payload))
    # sleep(10)
    
    # # Upload image with tinys3
    # s3 = boto3.client(
    #     's3',
    #     aws_access_key_id=ACCESS_KEY,
    #     aws_secret_access_key=SECRET_KEY,
    #     aws_session_token=SESSION_TOKEN
    # )
    # response = s3.upload_file(curdatetime + ".jpg", BUCKET_NAME, curdatetime + ".jpg")
    
    # os.system("rm translate")
    # os.system("rm " + curdatetime + ".jpg")
    return
