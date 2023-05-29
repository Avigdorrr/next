import pyttsx3

def main():
    text = 'first time i\'m using a package in next.py course'
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()




if __name__ == '__main__':
    main()