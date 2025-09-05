import os
import spacy
import yaml
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class FAQChatBot:
    """A chatbot designed to answer frequently asked questions (FAQs).

    This class initializes a ChatBot instance, loads FAQ data from a YAML file,
    and trains the bot to respond to user queries based on the provided FAQs.
    """
    def __init__(self):
        """Initialize the FAQChatBot with a ChatBot instance and load FAQ data."""
        # Initialize the ChatBot instance with a name
        self.bot = ChatBot('SmartFAQBot')
        # Initialize the NLP module for processing user input
        self.text_similarity_analyzer = TextSimilarityAnalyzer()
        # Load the FAQ data once from the YAML file
        self.faq_data = self.load_faq_data()
        # Train the bot with the FAQ dataset to learn the questions and answers
        self.train_bot()

    def load_faq_data(self):
        """Load FAQ data from a YAML file."""
        # Attempt to load the FAQ data from a YAML file
        try:
            # Get the directory of the current script
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the path to the YAML file
            file_path = os.path.join(current_dir, 'faq_dataset.yaml')
            # Open the YAML file for reading
            with open(file_path, 'r', encoding='utf-8') as file:
                # Load and return the list of FAQs from the YAML file
                return yaml.safe_load(file)['faqs']
        except FileNotFoundError:
            # Handle the case where the file is not found
            print("Error: FAQ dataset file not found.")
            return []  # Return an empty list if the file is not found
        except yaml.YAMLError as e:
            # Handle errors that occur while loading the YAML file
            print(f"Error loading YAML file: {e}")
            return []  # Return an empty list if there is a YAML error

    def train_bot(self):
        """Train the ChatBot with the loaded FAQ dataset."""
        # Create a trainer for the ChatBot using the ListTrainer
        trainer = ListTrainer(self.bot)
        training_data = []  # Initialize a list to hold training data
        
        # Iterate through each item in the FAQ data
        for item in self.faq_data:
            training_data.append(item['question'])  # Add the question
            training_data.append(item['answer'])    # Add the answer
        
        # Train the chatbot with the flat list of questions and answers
        trainer.train(training_data)  # Train with the flat list

    def get_response(self, input_text):
        """Get a response from the ChatBot based on user input."""
        # Set a similarity threshold for matching questions
        similarity_threshold = 0.7
        best_match = None  # Variable to store the best matching FAQ item
        highest_similarity = 0  # Variable to track the highest similarity score

        # Check for the best matching question based on similarity
        for item in self.faq_data:
            question = item['question']  # Get the current question from the FAQ
            # Calculate similarity between user input and the current FAQ question
            similarity = self.text_similarity_analyzer.get_similarity(input_text, question)
            # Update the best match if the current similarity is higher
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = item  # Store the current best match

        # If a suitable match is found, return the corresponding answer
        if highest_similarity >= similarity_threshold:
            return best_match['answer']

        # Return a default response if no match is found
        return "Sorry, I do not understand. Please, try again."

class TextSimilarityAnalyzer:
    """A module for natural language processing (NLP) tasks.

    This class utilizes the spaCy library to process text, extract entities,
    and calculate similarity between texts.
    """
    def __init__(self):
        """Initialize the TextSimilarityAnalyzer with the spaCy English model."""
        # Load the English NLP model from spaCy for processing text
        self.nlp = spacy.load("en_core_web_md")

    def extract_entities(self, text):
        """Extract entities from the input text."""
        # Process the input text with the NLP model to identify entities
        doc = self.nlp(text)
        # Extract and return entities as a list of tuples (entity text, entity label)
        return [(ent.text, ent.label_) for ent in doc.ents]

    def get_similarity(self, text1, text2):
        """Calculate the similarity score between two texts."""
        # Process both input texts with the NLP model to calculate similarity
        doc1 = self.nlp(text1)
        doc2 = self.nlp(text2)
        # Calculate and return the similarity score between the two texts
        return doc1.similarity(doc2)

if __name__ == "__main__":
    # Create an instance of the FAQChatBot
    chatbot = FAQChatBot()
    while True:
        # Prompt the user for input
        input_text = input("You: ")
        # Exit the loop if the user types 'exit'
        if input_text.lower() == 'exit':
            break
        # Get the chatbot's response to the user input
        response = chatbot.get_response(input_text)
        # Print the chatbot's response
        print(f"Bot: {response}")