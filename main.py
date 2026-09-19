import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("AQ.Ab8RN6KStuAnQwWFzMrY8KTVlFTDiOeaou9___xVxZWGIFRKEQ")
)

chat = client.chats.create(
    model="gemini-2.5-flash"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat_message():
    data = request.json
    user_message = data["message"]

    response = chat.send_message(user_message)

    return jsonify({
        "response": response.text
    })


if __name__ == "__main__":
    app.run(debug=True)
