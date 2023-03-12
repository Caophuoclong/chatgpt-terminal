import os
import platform
from ai.OpenAI import OpenAI
from dotenv import load_dotenv
from terminal.Terminal import Terminal


def main():
    try:
        message=input("Please type your question: ")
        load_dotenv()
        ai = OpenAI()
        terminal = Terminal()
        # if platform.system() == 'Windows':
        #     os.system('cls')
        # else:
        #     os.system('clear')
        exit_commands = terminal.get_exit_commands()
        if message in exit_commands:
            return
        terminal.wait()
        response = ai.ask(message)
        terminal.stop_wait()
        terminal.display_response(response.message)
        options = ["yes", "no"]
        user_input = ''
        input_message = "Would you like continue?\n"
        for index, item in enumerate(options):
            input_message += f'{index+1}) {item}\n'
        input_message += 'Your choice: '
        while user_input.lower() not in options:
            user_input = input(input_message)
            print(user_input)
        if user_input.lower() == options[0].lower():
            while True:
                message = terminal.get_user_message()
                if message in exit_commands:
                    break
                terminal.wait()
                response = ai.ask(message)
                terminal.stop_wait()
                terminal.display_response(response.message)
                print("Type `exit` to quit this conversation!")
        else:
            return


        
            
            # google_voice.speak(response.message, 'en')
            # pyttsx3_voice.speak(response.message)
    except OSError as e:
        pass


if __name__ == '__main__':
    main()
