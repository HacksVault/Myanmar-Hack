import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    if response and hasattr(response, 'text'):
        return response.text
    return "No valid response"

def chatbot_conversation():
    user_data = {
        "name": None,
        "age": None,
        "location": None,
        "contact_number": None,
        "issue": None,
        "issue_details": []
    }
    print("Bot: Hello! I'm here to help you. What's your name?")
    
    while True:
        user_input = input("You: ")

        if user_data["name"] is None:
            user_data["name"] = user_input
            print("Bot: Nice to meet you, {}! How old are you?".format(user_data["name"]))
            continue
            
        if user_data["age"] is None:
            user_data["age"] = user_input
            print("Bot: Thank you, {}! Where are you located?".format(user_data["name"]))
            continue
            
        if user_data["location"] is None:
            user_data["location"] = user_input
            print("Bot: Got it! What's your contact number?".format(user_data["name"]))
            continue
            
        if user_data["contact_number"] is None:
            user_data["contact_number"] = user_input
            print("Bot: Thank you! What issue are you facing? (water, health, food, emergency)")
            continue
        
        if user_data["issue"] is None:
            user_data["issue"] = user_input.lower()
            if user_data["issue"] not in ["water", "health", "food", "emergency"]:
                print("Bot: I'm sorry, I can only help with water, health, food, or emergency issues. Please specify your issue again.")
                continue
            
            print("Bot: Okay, you're facing an issue with {}.".format(user_data["issue"]))
        
            if user_data["issue"] == "water":
                follow_up_questions = [
                    "How much water is left for you?",
                    "How many people are there?"
                ]
            elif user_data["issue"] == "health":
                follow_up_questions = [
                    "How long have you had this problem?",
                    "Is anyone nearby for help, and do you have first-aid medication?"
                ]
            elif user_data["issue"] == "food":
                follow_up_questions = [
                    "How much food is left?",
                    "How many members are there?"
                ]
            elif user_data["issue"] == "emergency":
                follow_up_questions = [
                    "What is your emergency?",
                    "Is anyone nearby to help you?"
                ]
            
            for question in follow_up_questions:
                answer = input("Bot: {} ".format(question))
                user_data["issue_details"].append(answer)
            print("\nSummary of the collected information:")
            print(f"Issue Type: {user_data['issue'].capitalize()}")
            print(f"Name: {user_data['name']}")
            print(f"Age: {user_data['age']}")
            print(f"Location: {user_data['location']}")
            print(f"Contact Number: {user_data['contact_number']}")
            print("Issue Details:")
            for detail in user_data['issue_details']:
                print(f"- {detail}")
            break

chatbot_conversation()
