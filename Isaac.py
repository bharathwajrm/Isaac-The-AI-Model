import datetime
import pyttsx3
import random
import wikipedia
import webbrowser
import pyjokes
from translate import Translator as MicrosoftTranslator
import requests
from nltk.corpus import wordnet
import nltk


# Initialize the Pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Define the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Define the wishMe function
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("Isaac Here, How may I help you, sir?")

# Define the badDayResponse function
def badDayResponse():
    responses = [
        "It's okay, everyone has bad days.",
        "Don't worry, things will get better.",
        "Just remember, tomorrow is a new day.",
        "Sometimes life throws challenges, but you can overcome them.",
        "Sure, let's lighten the mood with a joke!"
    ]

    # Select a random response
    selected_response = random.choice(responses)

    return selected_response

# Define the goodDayResponse function
def goodDayResponse():
    responses = [
        "That's wonderful to hear! I hope your day gets even better.",
        "I'm glad to hear that. Keep spreading positivity!",
        "Fantastic! Let's make the most of this great day.",
        "A good day indeed! If there's anything I can do to make it better, just let me know.",
        "Awesome! Your positive energy is contagious."
    ]

    # Select a random response
    selected_response = random.choice(responses)

    return selected_response

#define the goodbyeResponse function

def goodbyeResponse():
    responses = [
        "Goodbye! Have a fantastic day!",
        "Take care and goodbye!",
        "Farewell! Remember to smile.",
        "Until next time! Keep spreading positivity.",
        "Goodbye for now. Your positive energy is appreciated."
    ]

    selected_response = random.choice(responses)

    return selected_response

#define the greetingResponse function

def greetingResponse():
    responses = [
        "Hello! Welcome to our community!",
        "Hi there! It's great to have you!",
        "Welcome! We're glad you're here!",
        "Hey! Thanks for joining us!",
        "Hi! We hope you'll enjoy your time with us!"
    ]
    selected_response = random.choice(responses)

    return selected_response

#define the howAreYouResponse function

def howAreYouResponse():
    responses = [
        "I'm just a computer program, but I'm here to help you!",
        "I don't have feelings, but I'm ready to assist you!",
        "I'm here and ready to assist you with any questions!",
        "I'm functioning well and eager to help you out!",
        "I'm just a bunch of code, but I'm at your service!"
    ]
    selected_response = random.choice(responses)

    return selected_response

#define the howIsYourDayResponse function

def howIsYourDayResponse():
    responses = [
        "I don't experience days, but I'm here and ready to assist you!",
        "Since I'm not human, I don't have days, but I'm here to help!",
        "I'm always available and ready to help, regardless of the time!",
        "I'm a program, so I don't have days, but I'm here for you!",
        "Every day is the same for me, but I'm here to assist you as always!"
    ]
    selected_response = random.choice(responses)

    return selected_response

#define to get time and date

def get_current_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

#define meaning

def get_word_meaning(word):
    meanings = wordnet.synsets(word)


    if meanings:
        meaning_str = ""
        for synset in meanings:
            meaning_str += f"{synset.definition()}\n"
        return meaning_str
    else:
        return "Word not found in the dictionary."

def get_word_explanation(word):
    meanings = wordnet.synsets(word)

    if meanings:
        return meanings[0].definition()
    else:
        return "Word not found in the dictionary."

# Define a function to translate text

def translate_text(text, target_language='en'):
    translator = MicrosoftTranslator(to_lang=target_language)
    translated_text = translator.translate(text)
    return translated_text

#define mediabot

def get_news(api_key, category="general"):
    base_url = "http://api.mediastack.com/v1/news"
    params = {
        "access_key": api_key,
        "categories": category
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    articles = data.get("data", [])
    return articles

#define weatherbot
def get_category_choice():
    categories = {
        "1": "business",
        "2": "entertainment",
        "3": "health",
        "4": "science",
        "5": "sports",
        "6": "technology"
    }

    print("Select a category:")
    for key, value in categories.items():
        print(f"{key}. {value.capitalize()}")

    choice = input("Enter the number: ")
    return categories.get(choice)


# Define the main function to run Isaac
def run_Isaac():
    wishMe()
    while True:
        query = input("you:").lower()

        if 'bye' in query:
            isaac_response = goodbyeResponse()
            print("isaac:", isaac_response)
            speak(isaac_response)
            break

        elif any(keyword in query for keyword in
                 ['bad day', 'worst day', 'terrible day', 'awful day', 'rough day', 'not going well', 'feeling down',
                  'having a tough time', 'emotional day', 'mentally exhausted', 'challenging day', 'overwhelming day',
                  'disastrous day', 'disheartening day', 'frustrating day', 'irritating day']):
            isaac_response = badDayResponse()
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif any(keyword in query for keyword in
                 ['good day', 'great day', 'awesome day', 'fantastic day', 'amazing day', 'excellent day',
                  'wonderful day',
                  'fabulous day', 'terrific day', 'productive day', 'happy day', 'joyful day', 'positive day',
                  'fulfilling day', 'pleasant day']):
            isaac_response = goodDayResponse()
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif any(keyword in query for keyword in ['hi', 'hey', 'hello', 'greetings', 'howdy', 'isaac', 'Isaac']):
            isaac_response = greetingResponse()
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif any(keyword in query for keyword in ['how are you', 'how\'s it going', 'how do you do', 'are you well']):
            isaac_response = howAreYouResponse()
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif any(keyword in query for keyword in ['how was your day', 'how\'s your day', 'how did your day go', 'what about today']):
            isaac_response = howIsYourDayResponse()
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif any(keyword in query for keyword in
                 ['wikipedia', 'what is', 'what', 'tell me about', 'find in wikipedia', 'how']):
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("Would you like a one-line summary or a detailed response?")
            user_choice = input("you: ").lower()

            while user_choice not in ['1', '2']:
                speak("Please choose between 'one-line' type 1 and 'detailed' type 2.")
                user_choice = input("you: ").lower()

            if user_choice == '1':
                isaac_response = results
            else:
                detailed_results = wikipedia.summary(query)
                isaac_response = "Here's a detailed response from Wikipedia: " + detailed_results

            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif 'open youtube' in query or 'youtube' in query or 'y' in query:
            isaac_response = "opening youtube...!"
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open("https://www.youtube.com")
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif 'open google' in query or 'google' in query or 'g' in query:
            isaac_response = "opening Google...!"
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open("https://www.google.com")
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif 'open instagram' in query or 'instagram' in query or 'i' in query:
            isaac_response = "opening Insta...!"
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open("https://www.instagram.com")
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif 'open whatsapp' in query or 'whatsapp' in query or 'w' in query:
            isaac_response = "opening WhatsApp..."
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open("https://web.whatsapp.com")
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif 'open snapchat' in query or 'snapchat' in query or 's' in query:
            isaac_response = "opening snapchat..."
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open("https://web.snapchat.com")
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif 'jokes' in query or 'joke' in query or 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            isaac_response = "here is joke for you " + joke
            print("Isaac:", isaac_response)
            speak(isaac_response)

        elif 'time' in query or 'what is the time' in query or 'what is the date' in query or 'date' in query:
            current_time = get_current_time()
            time_response = "The current time is: " + current_time
            print("Isaac:", time_response)
            speak(time_response)

        elif 'm' in query or 'meaning of' in query:
            nltk.download("wordnet")

            print("Welcome to the DictoBot!")
            speak("Welcome to the DictoBot!")

            choice = input("Enter '1' for word meaning or '2' for one-line explanation (Press 'q' to quit): ")
            if choice == 'q':
                break
            word = input("Enter a word: ")

            if choice == '1':
                meaning = get_word_meaning(word)
                print(meaning)
                speak(meaning)

            elif choice == '2':
                explanation = get_word_explanation(word)
                print(explanation)
                speak(explanation)

        elif 't' in query or 'translate' in query:
            print("Welcome to the Language Translation Bot!")
            speak("Welcome to the Language Translation Bot!")

            while True:
                text_to_translate = input("Enter the text you want to translate (type 'exit' to quit): ")
                if text_to_translate.lower() == 'exit':
                    break

                print("\nCommonly used languages:")
                print("1. English")
                print("2. French")
                print("3. Spanish")
                print("4. German")
                print("5. Italian")
                print("6. Tamil")
                print("7. Hindi")
                print("8. Custom language (Enter language code)")
                option = input("\nEnter the option number or language code: ")

                if option == '1':
                    target_language = 'en'

                elif option == '2':
                    target_language = 'fr'

                elif option == '3':
                    target_language = 'es'

                elif option == '4':
                    target_language = 'de'

                elif option == '5':
                    target_language = 'it'

                elif option == '6':
                    target_language = 'ta'

                elif option == '7':
                    target_language = 'hi'
                elif option == '8':
                    target_language = input("Enter the language code: ")

                else:
                    print("Invalid option. Translating to English by default.")
                    target_language = 'en'
                translated_text = translate_text(text_to_translate, target_language)
                print(f"\nTranslated Text: {translated_text}")

        elif 'n' in query or 'article' in query:
            api_key = "4b41612000d274eb2b461c03a6f508a5"

            print("Hii!..I'm mediabot here to serve you news and articles")
            speak("Hii!..I'm mediabot here to serve you news and articles")

            while True:
                choice = input("Enter '1' for live news or '2' for articles (Press 'q' to quit): ")

                if choice == 'q':
                    break

                category = get_category_choice()
                if category is None:
                    print("Invalid category selection.")
                    continue

                news_list = get_news(api_key, category)

                if not news_list:
                    print("No news or articles found.")
                    continue

                for idx, news in enumerate(news_list, start=1):
                    print(f"{idx}. {news['title']}")
                    print(news['description'])
                    print("=" * 50)

                listen_choice = input("Do you want to listen? (y/n): ")
                if listen_choice.lower() == 'y':
                    full_news = "\n".join(
                        [f"{idx}. {news['title']}. {news['description']}" for idx, news in
                         enumerate(news_list, start=1)])
                    speak(full_news)

        elif 'w1' in query:
            print("\t\tWelcome to the Weather bot\n\n")
            speak("Welcome to the Weather bot")
            print("Just Enter the City you want the weather report!\n")

            city_name = input("Enter the name of the City : ")
            print("\n")

            # Function to Generate Report
            def Gen_report(C):
                url = 'https://wttr.in/{}'.format(C)
                try:
                    data = requests.get(url)
                    T = data.text
                except:
                    T = "Error Occurred"
                print(T)

            Gen_report(city_name)




    else:
            isaac_response = "I'm sorry, I didn't quite understand that."
            print("isaac:", isaac_response)
            speak(isaac_response)



# Run the assistant

run_Isaac()