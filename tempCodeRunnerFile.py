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