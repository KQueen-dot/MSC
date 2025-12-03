import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()

engine = pyttsx3.init()

print("""Busqueda iniciada. Diga la palabra comando para buscar entre nuestros sitios web disponibles: 
Amazon, Youtube Music, Shein, Temu, Mercado libre, Walmart, Spotify, Wikipedia, Playstore y Tiktok""")

def talk():
    mic = sr.Microphone()
    while True:
        with mic as source:
            audio = recognizer.listen(source)


        try:
            text = recognizer.recognize_google(audio, language = 'Es')
            print(f'Haz dicho: {text}')
            return text.lower()
        except sr.UnknownValueError:
            print("No se detecto ninguna entrada de voz. Por favor, intentelo de nuevo")

ear = talk()

if 'amazon' in ear: 
    engine.say('Que es lo que quieres buscar en amazon')
    engine.runAndWait()
    search = talk()
    webbrowser.open(f'https://www.amazon.es/s?k={search}')
    
elif 'music' in ear: 
    engine.say('Que es lo que quieres buscar en Youtube Music')
    engine.runAndWait()
    search = talk()
    webbrowser.open(f'https://music.youtube.com/search?q={search}')

elif 'shein' in ear: 
    engine.say('Que es lo que quieres buscar en Shein')
    engine.runAndWait()
    search = talk()
    webbrowser.open(f'https://www.shein.com.mx/pdsearch/{search}')

elif 'temu' in ear: 
    engine.say('Que es lo que quieres buscar en temu')
    engine.runAndWait()
    search = talk()
    webbrowser.open(f'https://www.temu.com/search_result.html?search_key={search}')

elif 'mercado' in ear: 
    engine.say('Que es lo que quieres buscar en mercado libre')
    engine.runAndWait()
    search = talk()
    webbrowser.open(f'https://listado.mercadolibre.com.mx/{search}')

elif 'walmart' in ear: 
    engine.say('Que es lo que quieres buscar en walmart')
    engine.runAndWait()
    search = talk()
    webbrowser.open(f'https://www.walmart.com.mx/search?q={search}')

elif 'spotify' in ear: 
    engine.say('Que es lo que quieres buscar en spotify')
    engine.runAndWait()
    search = talk()
    webbrowser.open(f'https://open.spotify.com/search/{search}')

elif 'wikipedia' in ear: 
    engine.say('Que es lo que quieres buscar en wikipedia')
    engine.runAndWait()
    search = talk()
    webbrowser.open(f'https://es.wikipedia.org/wiki/{search}')

elif 'play' in ear: 
    engine.say('Que es lo que quieres buscar en Play Store')
    engine.runAndWait()
    search = talk()
    webbrowser.open(f'https://play.google.com/store/search?q={search}')

elif 'tiktok' in ear: 
    engine.say('Que es lo que quieres buscar en tiktok')
    engine.runAndWait()
    search = talk()
    webbrowser.open(f'https://www.tiktok.com/search?q={search}')

else:
    print("No se detecto ninguna entrada de voz. Por favor, intentelo de nuevo")