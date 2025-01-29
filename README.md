# Personalized Chatbot

A web-based chatbot with **text, speech recognition, and text-to-speech** capabilities. The chatbot uses **Google Generative AI** to generate responses and supports **image generation**.

## Features

- 💬 **Interactive Chat** - Communicate with the bot via text.
- 🗣️ **Speech Recognition** - Speak to the chatbot using voice input.
- 🔊 **Text-to-Speech** - The bot can respond with audio.

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask  
- **APIs:** Google Generative AI  
- **Libraries:** SpeechRecognition, gTTS  

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/personalized-chatbot.git
   cd personalized-chatbot
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Flask server:
   ```sh
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## API Usage

- **Chat Endpoint:** `POST /chat`
  - Request: `{ "message": "Hello" }`
  - Response: `{ "response": "Hi there!" }`  

## Environment Variables

To use Google Generative AI, set up your API key in `.env`:
```sh
GOOGLE_API_KEY=your_api_key_here
```
Or replace `genai.configure(api_key="...")` with a secure method.

## Contributing

Feel free to submit issues or pull requests.  


