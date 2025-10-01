from chatbot import FAQChatBot

def test_chatbot():
    """Test the FAQChatBot's responses against predefined test cases.

    This function defines a list of test cases, each containing a question
    and the expected answer. It creates an instance of the FAQChatBot,
    checks the responses for each test case, and calculates the accuracy
    of the chatbot based on the number of correct matches.
    """
    # Define a list of test cases with questions and their expected answers
    test_cases = [
        ("What services do you offer?", "I provide RPA, Python, and AI-driven automation."),
        ("Where are you located?", "I work remotely, based in the U.S."),
        ("How can I contact you?", "You can reach me via email at example@example.com.")
    ]
    
    # Create an instance of the FAQChatBot
    chatbot = FAQChatBot()
    correct_matches = 0

    # Iterate through each test case
    for question, expected_answer in test_cases:
        # Get the chatbot's response for the current question
        response = chatbot.get_response(question)
        # Check if the response matches the expected answer
        if response == expected_answer:
            correct_matches += 1  # Increment the counter for correct matches
            print(f"Test Passed: {question}")
        else:
            # Print the details of the failed test case
            print(f"Test Failed: {question} | Expected: {expected_answer}, Got: {response}")

    # Calculate and print the accuracy of the chatbot
    if test_cases:  # Check to avoid division by zero
        accuracy = (correct_matches / len(test_cases)) * 100
        print(f"Accuracy: {accuracy:.2f}%")  # Format accuracy to two decimal places
    else:
        print("No test cases to evaluate.")

# Run the test function
if __name__ == "__main__":
    test_chatbot()