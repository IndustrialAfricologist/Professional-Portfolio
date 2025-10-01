# Smart FAQ Chatbot with NLP Enhancements

## Project Overview
This project implements a lightweight FAQ-style chatbot using **ChatterBot** for conversation management and **spaCy** for natural language understanding. The chatbot is designed to handle frequently asked questions for small businesses or freelancers, providing quick and accurate responses through a web interface.

## Features
- **Basic Conversational Flow**: Trained on a simple FAQ dataset stored in a YAML file.
- **NLP Enrichment**: Utilizes spaCy to extract entities and calculate similarity scores for fuzzy queries, enhancing the chatbot's understanding of user input.
- **Web Interface**: Provides a user-friendly web interface for interaction, allowing users to ask questions and receive responses in real-time.
- **FAQ Dataset Extensibility**: Easily update the knowledge base by modifying the `faq_dataset.yaml` file.
- **Evaluation Metrics**: Includes a test script to evaluate performance using a simple accuracy metric.

## Requirements
- Python 3.x
- ChatterBot
- spaCy
- PyYAML
- Flask

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd smart_faq_chatbot
   ```

2. Install the required packages:
   ```bash
   pip install chatterbot spacy pyyaml flask
   ```

3. Download the spaCy model:
   ```bash
   python -m spacy download en_core_web_md
   ```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
   Open your web browser and navigate to `http://127.0.0.1:5000/` to interact with the chatbot through the web interface.

2. To test the chatbot's accuracy, run:
   ```bash
   python test_chatbot.py
   ```

## FAQ Dataset
The FAQ dataset is stored in `faq_dataset.yaml` and contains the following entries:
```yaml
faqs:
  - question: "What services do you offer?"
    answer: "I provide RPA, Python, and AI-driven automation."
  - question: "Where are you located?"
    answer: "I work remotely, based in the U.S."
  - question: "How can I contact you?"
    answer: "You can reach me via email at example@example.com."
```

## Code Structure
- `chatbot.py`: Contains the implementation of the FAQ chatbot, including the training and response logic.
- `faq_dataset.yaml`: The YAML file that holds the FAQ data.
- `test_chatbot.py`: A script to test the accuracy of the chatbot against predefined questions and answers.
- `app.py`: The Flask application that provides a web interface for user interaction with the chatbot.
- `templates/index.html`: The HTML template for the chatbot's web interface.

## Testing
The `test_chatbot.py` script defines a list of test cases with questions and their expected answers. It evaluates the chatbot's responses and calculates the accuracy based on correct matches.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.

## License
This project is licensed under the MIT License.
```