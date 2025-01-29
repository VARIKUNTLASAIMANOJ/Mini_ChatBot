from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

genai.configure(api_key="AIzaSyASZ6NYMYYA2RL2ZT1tgxOv36EP9DVJR5k")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    
    if user_message.lower().startswith("generate image of"):
        image_url = generate_image(user_message.replace("generate image of", "").strip())
        return jsonify({"image_url": image_url})

    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

def get_bot_response(message):
    """Fetch response from Gemini AI with multi-language support."""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        return "I couldn't process that request."

def generate_image(prompt):
    """Generate an image using Google Gemini."""
    try:
        model = genai.GenerativeModel("gemini-pro-vision")
        response = model.generate_content(prompt)
        return response.media[0].url if response.media else None
    except Exception as e:
        return None

if __name__ == "__main__":
    app.run(debug=True)