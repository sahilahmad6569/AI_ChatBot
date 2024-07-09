# AI ChatBot

Welcome to the AI ChatBot project! This project demonstrates a chatbot built using Python, Google Generative AI, and PyAutoGUI for automating interactions with a messaging application like WhatsApp.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Automated Messaging**: Interacts with a messaging application to send automated replies.
- **Generative AI**: Utilizes Google's Generative AI to generate responses based on chat history.
- **Multi-language Support**: Capable of generating responses in Hindi, Urdu, English, and so on.
- **Cursor Coordinates Utility**: Includes a script to find accurate screen coordinates for automation.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your computer.
- Required Python libraries: `google.generativeai`, `pyautogui`, `pyperclip`.
- Google Generative AI API key set as an environment variable (`GEMINI_API_KEY`).

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/sahilahmad6569/AI_ChatBot.git
    cd AI_ChatBot
    ```

2. **Install the Required Libraries**

    ```bash
    pip install google-generativeai pyautogui pyperclip
    ```

3. **Set Up the API Key**

    Ensure your Google Generative AI API key is set as an environment variable:

    ```bash
    export GEMINI_API_KEY=your_api_key_here
    ```

## Usage

1. **Run the Cursor Position Utility**

    Use `cursor.py` to find the screen coordinates for automation:

    ```bash
    python cursor.py
    ```

    Move your mouse to the required positions and note the coordinates printed in the console.

2. **Update `main.py` with the Coordinates**

    Update the `pyautogui.click`, `pyautogui.moveTo`, and other coordinate-specific lines with the values obtained from `cursor.py`.

3. **Run the ChatBot**

    Start the chatbot:

    ```bash
    python main.py
    ```

    The script will wait for 5 seconds to allow you to switch to the messaging application. Ensure the application is open and ready to interact.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [Google Generative AI](https://developers.google.com/generative-ai)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- [Pyperclip](https://pypi.org/project/pyperclip/)

