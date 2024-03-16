import tkinter as tk
import speech_recognition as sr

def transcribe_speech():
    global output_label
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        output_label.config(text="Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)  # Adjust timeout as needed
            output_label.config(text="Transcribing...")
            text = recognizer.recognize_google(audio)
            output_label.config(text="You said: " + text)
        except sr.UnknownValueError:
            output_label.config(text="Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            output_label.config(text="Could not request results; {0}".format(e))

# Create the main window
root = tk.Tk()
root.title("Speech to Text")

# Create and configure widgets
header_label = tk.Label(root, text="Speech to Text", font=("Arial", 16))
header_label.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack(pady=10)

transcribe_button = tk.Button(root, text="Transcribe", command=transcribe_speech)
transcribe_button.pack(pady=10)

# Run the application
root.mainloop()
