"""
Simple Speech to Text Test
No hotkeys - just press Enter to record
"""

import speech_recognition as sr
from pynput.keyboard import Controller
import time

# Initialize
recognizer = sr.Recognizer()
keyboard_controller = Controller()

def type_text(text):
    """Type the text"""
    print(f"Typing: {text}")
    time.sleep(0.5)  # Give you time to click into a text field
    for char in text:
        keyboard_controller.type(char)
    keyboard_controller.type(' ')

def record_and_transcribe():
    """Record audio and transcribe to text"""
    print("\n[*] Recording... Speak now (you have 10 seconds)")

    with sr.Microphone() as source:
        # Adjust for ambient noise
        print("[*] Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            print("[*] Listening...")
            # Record audio
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

            print("[*] Processing speech...")

            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio, language='en-US')

            print(f"[+] Transcribed: {text}")

            # Type the text
            print("[*] Text will be typed in 2 seconds - click into a text field now!")
            time.sleep(2)
            type_text(text)
            print("[+] Done!")

        except sr.WaitTimeoutError:
            print("[-] No speech detected (timeout)")
        except sr.UnknownValueError:
            print("[-] Could not understand audio")
        except sr.RequestError as e:
            print(f"[-] Could not request results; {e}")
        except Exception as e:
            print(f"[-] Error: {e}")

def main():
    """Main function"""
    print("=" * 60)
    print("Speech to Text Test")
    print("=" * 60)
    print("\nThis test will:")
    print("1. Record your voice when you press Enter")
    print("2. Transcribe it to text")
    print("3. Type it into your active window")
    print("\nPress Ctrl+C to exit\n")

    try:
        while True:
            input("Press Enter to start recording...")
            record_and_transcribe()
            print("\n" + "=" * 60)
    except KeyboardInterrupt:
        print("\n\nExiting...")

if __name__ == "__main__":
    main()
