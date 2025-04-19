import google.generativeai as genai
from IPython.display import Markdown
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the generative AI model
genai.configure(api_key=api_key)
flash = genai.GenerativeModel('gemini-1.5-flash')
chat = flash.start_chat(history=[])

def chatbot():
    print("Chatbot is ready! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Get a response from the chatbot
        response = chat.send_message(user_input)
    
        # Display the response in markdown format
        print("Bot: ", (response.text))

# Start the chatbot
if __name__ == "__main__":
    chatbot()
