import os
import shutil
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini Client
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

TARGET_DIR = "./Unsorted"

# Ensure target and destination directories exist
CATEGORIES = ["Invoices", "Code", "Logs", "Docs", "Misc"]

def categorize_file(filename, content_sample):
    prompt = f"""
    You are an automated file sorter.
    Based on the filename and content snippet below, classify the file into EXACTLY ONE of these categories:
    {', '.join(CATEGORIES)}

    Filename: {filename}
    Content Snippet:
    {content_sample[:500]}

    Respond with ONLY the category name. Do not include markdown or extra text.
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    
    category = response.text.strip()
    return category if category in CATEGORIES else "Misc"

def run_organizer():
    if not os.path.exists(TARGET_DIR):
        print(f"Directory '{TARGET_DIR}' does not exist.")
        return

    files = [f for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f))]
    if not files:
        print("No files found to organize.")
        return

    print("🤖 Lazy Inbox Cleaner running...\n")

    for file in files:
        filepath = os.path.join(TARGET_DIR, file)
        try:
            with open(filepath, "r", errors="ignore") as f:
                content = f.read(500)
        except Exception:
            content = ""

        category = categorize_file(file, content)
        dest_dir = os.path.join(TARGET_DIR, category)
        os.makedirs(dest_dir, exist_ok=True)
        
        shutil.move(filepath, os.path.join(dest_dir, file))
        print(f"📁 Moved '{file}' ➔ {category}/")

    print("\n✨ Done! Your inbox is clean.")

if __name__ == "__main__":
    run_organizer()