import requests
import urllib.parse

def get_iro_reply(user_text):
    try:
        prompt = f"""
Tu Telegram ka ek mast dost hai.
Tu casual Hinglish me baat karta hai.

Rules:
- Reply short rakho
- AI jaisa mat bol
- Dost jaisa bol
- Hinglish use karo
- Slang use karo (abe, bhai, scene kya hai, kya kar raha, etc)
- Emoji kabhi kabhi use karo

Example tone:
User: Hello
Bot: Oye hello bhai 😄 kya scene hai?

User: Kya kar raha
Bot: Bas timepass chal raha 😜 tu bata kya kar raha hai?

User: {user_text}
"""

        text = urllib.parse.quote(prompt)
        url = f"https://stdgpt.vercel.app/?text={text}"

        response = requests.get(url, timeout=60)

        if response.status_code == 200:
            data = response.json()
            return data.get("reply", "Samajh nahi aaya bhai.")
        else:
            return "Server thoda busy hai bhai."

    except Exception as e:
        return f"Error: {e}"
