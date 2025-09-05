from flask import Flask, request, render_template
from chatbot import FAQChatBot

# Initialize the Flask application
app = Flask(__name__)

# Create an instance of the FAQChatBot
chatbot = FAQChatBot()

@app.route('/')
def home():
    """Render the main page with the chat interface."""
    return render_template('index.html')  # Render the main page with the chat interface

@app.route('/ask', methods=['POST'])
def ask():
    """Handle user questions and return chatbot responses."""
    input_text = request.form['question']  # Get the question from the form
    response = chatbot.get_response(input_text)  # Get the chatbot's response
    return render_template('index.html', user_input=input_text, response=response)  # Render the response

if __name__ == "__main__":
    app.run(debug=True)  # Run the application in debug mode; set to False for production