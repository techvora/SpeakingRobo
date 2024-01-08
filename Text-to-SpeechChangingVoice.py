import pyttsx3
from tkinter import *

# Create tkinter window
root = Tk()

# Styling the frame which helps to make our background stylish
frame1 = Frame(root, bg="lightPink", height="150")
frame1.pack(fill=X)

frame2 = Frame(root, bg="lightgreen", height="750")
frame2.pack(fill=X)

# Styling the label which shows the text in our tkinter window
label = Label(frame1, text="Text to Speech", font="bold, 30", bg="lightpink")
label.place(x=180, y=70)

# Entry is used to enter the text
entry = Entry(frame2, width=45, bd=4, font=14)
entry.place(x=130, y=52)
entry.insert(0, "")


# Define a function which can get text and convert it into speech
def play():
    # Initialize the converter
    converter = pyttsx3.init()

    # Set properties before adding things to say
    converter.setProperty('rate', 150)  # Sets speed percent (can be more than 100)
    converter.setProperty('volume', 0.7)  # Set volume (0.0 to 1.0)

    # Get the entered text
    text = entry.get()

    # Queue the text to be spoken
    converter.say(text)

    # Empties the say() queue
    # Program will not continue until all speech is done talking
    converter.runAndWait()


# Create a button that holds our play function using command=play
btn = Button(frame2, text="SUBMIT", width="15", pady=10, font="bold, 15", command=play, bg='yellow')
btn.place(x=250, y=130)

# Give a title
root.title("text_to_speech_converter")

# Set window size
root.geometry("650x550+350+200")

# Start the GUI
root.mainloop()
