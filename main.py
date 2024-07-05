import google.generativeai as genai
import pyautogui
import time
import pyperclip
import os

# Configuring generative AI by Google
gemini_api_key = os.environ.get("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Generating response
def generate_response(chat_history) -> str:
        prompt = f"You are Sahil Ahmad and Indian religious 18 years old Computer Science student. You can speak Hindi, Urdu as well as English. This is the chat history: {chat_history}. Your response should be the next reply (response should contain only the message and nothing else)"
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        print(response_text)
        return response_text

# Checking if I have just messaged
def is_last_message_mine(chat_log, my_name="."):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if my_name in messages:
        return True 
    return False
    

def main():

    # Allow time to switch to the application where we want to perform the actions
    time.sleep(5)

    # Click on Whatsapp Icon 
    # pyautogui.click(854, 1012)
    # time.sleep(1)  # Add a small delay to ensure the click is registered

    while True:
        # Drag and select text
        pyautogui.moveTo(594, 292)
        pyautogui.mouseDown()
        pyautogui.moveTo(1849, 970, duration=1)  # You can adjust the duration as needed;
        pyautogui.mouseUp()
        time.sleep(1)  # Add a small delay to ensure the drag is completed

        # Copy the selected text (usually Ctrl+C)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)  # Add a small delay to ensure the text is copied

        # Deselect text by clicking on a blank position
        pyautogui.click(607, 299)

        # Retrieve the text from the clipboard
        chat_history = pyperclip.paste()

        # Print the selected text
        print(chat_history)

        # Checking if the last message is from the sender
        if(not is_last_message_mine(chat_history)):

            response = generate_response(chat_history)

            # Sending reply
            pyperclip.copy(response)
            pyautogui.click(1299, 1016)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')


if __name__ == "__main__":
    main()