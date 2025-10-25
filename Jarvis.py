import speech_recognition as sr # Converts speech (voice) into text
import pyttsx3  # Converts text to voice
import webbrowser  # Converts text to speech such as You Tube, Google and others
import os # os used for systems. such as shutdown and reset
import datetime  # Gets current date and time

def speak(text):
    engine = pyttsx3.init() # Initialize text-to-speech engine
    engine.say(text) # Add text to speech
    engine.runAndWait() 

def take_command(): # Function: Take voice input from user and convert it to text
    r = sr.Recognizer() # Create recognizer object
    with sr.Microphone() as source: # Use default microphone as input
        print("🎧Listening...")
        audio = r.listen(source,phrase_time_limit=4)

    try:
        print("✅jarvis active..")
        query = r.recognize_google(audio) # Convert recorded audio into text using Google Speech API
        print(f"You said: {query}") 
        return query.lower() # Return user command in lowercase
    except:
        return "" # If voice not recognized, return empty string

def perform_task(command): # Function: Perform task based on recognized command
    if "jarvis" in command:  # Respond when user says "Jarvis"
        speak("🤖Ya")
        print("Ya")

    elif "open youtube" in command:
        speak("🖥️Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("🌐Opening Google")
        webbrowser.open("https://google.com")

    elif "close the system" in command:
        speak("⚡shutdown your System.")
        os.system("shutdown /s /t 3") # shutdown your pc in 3 seconds
        return "exit" # Exit main loop

    elif "restart" in command:
        speak("Restarting your system")
        os.system("shutdown /r /t 3") # restart your pc in 3 seconds   

    elif "time" in command:
        exect_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {exect_time}")
        print("⏰ The time is:", exect_time) # see current time

    elif "today" in command:
        date = datetime.datetime.now().strftime("%d %m %Y")
        speak(f"Date of today is: {date}")
        print("📅Date is:", date) # see today's date

    else:
        speak("🤖Sorry, i am not understand this command.")

# main program
if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I help you?") # Greeting message when program starts
    while True: # Infinite loop listening for commands
        command = take_command() # Take user voice input
        if command: # If command is not empty
            result = perform_task(command) # if command is not empty, then it command perform 
            if result == "exit": # Exit the program when pc shutdown
                break
