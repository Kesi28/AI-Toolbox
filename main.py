"""
AI Toolbox - Text Processing Tool (New Version)
Author: Chan Ke Si
Using the new google-genai SDK
"""

from google import genai
import sys

# ==================== API Configuration ====================
API_KEY = "AIzaSyBa9cDjRpCkPn47gTUxD9AT9zlITTEvvVI"

client = genai.Client(api_key=API_KEY)

# ==================== Feature Functions ====================

def call_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

def text_summarizer(text):
    prompt = f"Please summarize the following content in one sentence:\n\n{text}"
    return call_gemini(prompt)

def email_polisher(draft):
    prompt = f"""Please rewrite the following email draft into a more formal and professional version. Keep the original meaning but improve grammar and tone.

Draft:
{draft}

Output the polished email:"""
    return call_gemini(prompt)

def translator(text, target_language="English"):
    prompt = f"Please translate the following content into {target_language}:\n\n{text}"
    return call_gemini(prompt)

def code_commentator(code):
    prompt = f"""Please add detailed comments to the following code, explaining each line or key section:

Code:
{code}

Output the code with comments:"""
    return call_gemini(prompt)

def todo_classifier(todo_list):
    prompt = f"""Please organize the following todo items into categories such as: Work, Study, Life, Shopping, Health. Output as a list.

Todo items:
{todo_list}

Output the categorized results:"""
    return call_gemini(prompt)

# ==================== Main Menu ====================

def show_menu():
    print("\n" + "="*40)
    print("🤖 AI Toolbox - Text Processing Tool")
    print("="*40)
    print("1. 📝 Summarizer")
    print("2. ✉️  Email Polisher")
    print("3. 🌐 Translator")
    print("4. 💬 Code Commentator")
    print("5. 📋 Todo Classifier")
    print("6. 🚪 Exit")
    print("-"*40)

def main():
    while True:
        show_menu()
        choice = input("Please choose (1-6): ").strip()
        
        if choice == "1":
            print("\n【Summarizer】Enter text (press Enter twice when done):")
            lines = []
            empty_count = 0
            while True:
                line = input()
                if line == "":
                    empty_count += 1
                    if empty_count == 2:
                        break
                else:
                    lines.append(line)
                    empty_count = 0
            text = "\n".join(lines)
            print("\n⏳ Generating summary...")
            result = text_summarizer(text)
            print("\n✅ Summary:\n", result)
            
        elif choice == "2":
            print("\n【Email Polisher】Enter your draft (press Enter twice when done):")
            lines = []
            empty_count = 0
            while True:
                line = input()
                if line == "":
                    empty_count += 1
                    if empty_count == 2:
                        break
                else:
                    lines.append(line)
                    empty_count = 0
            draft = "\n".join(lines)
            print("\n⏳ Polishing...")
            result = email_polisher(draft)
            print("\n✅ Polished email:\n", result)
            
        elif choice == "3":
            print("\n【Translator】")
            text = input("Enter text to translate: ")
            print("Target language: 1. English  2. Chinese  3. Malay")
            lang_choice = input("Choose (1/2/3): ")
            lang_map = {"1": "English", "2": "Chinese", "3": "Malay"}
            target = lang_map.get(lang_choice, "English")
            print("\n⏳ Translating...")
            result = translator(text, target)
            print("\n✅ Translation:\n", result)
            
        elif choice == "4":
            print("\n【Code Commentator】Paste your code (press Enter twice when done):")
            lines = []
            empty_count = 0
            while True:
                line = input()
                if line == "":
                    empty_count += 1
                    if empty_count == 2:
                        break
                else:
                    lines.append(line)
                    empty_count = 0
            code = "\n".join(lines)
            print("\n⏳ Generating comments...")
            result = code_commentator(code)
            print("\n✅ Code with comments:\n", result)
            
        elif choice == "5":
            print("\n【Todo Classifier】Enter todo items separated by commas:")
            todos = input("Todo items: ")
            print("\n⏳ Classifying...")
            result = todo_classifier(todos)
            print("\n✅ Categorized results:\n", result)
            
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    if API_KEY == "your API_KEY":
        print("⚠️  Please configure your API Key first!")
        print("   Replace 'your API_KEY' on line 12 with your actual API Key")
        print("   Get your API Key: https://aistudio.google.com/app/apikey")
    else:
        print("🚀 AI Toolbox started successfully!")
        main()