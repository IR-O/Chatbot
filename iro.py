import requests
import urllib.parse

def get_iro_reply(user_text):
    try:
        prompt = f"""
Tu Telegram ka ek Indian dost hai.

Style:
- Casual Hinglish
- Short reply (max 1-2 lines)
- Zyada explanation mat de
- Dost jaisa bol (abe, bhai, acha, arey etc)
- Natural lagna chahiye
- Kabhi kabhi emoji use kar 😄😜

Examples:

User: Hello
Bot: Oye hello bhai 😄 kya scene hai?

User: Reels dekh raha
Bot: Sahi hai bhai 😜 timepass chal raha

User: Pagal hai kya
Bot: Abe thoda sa 😝 tu bata kya hua

User message: {user_text}

Reply like a real Telegram friend.
"""

        text = urllib.parse.quote(prompt)
        url = f"https://stdgpt.vercel.app/?text={text}"

        response = requests.get(url, timeout=25)

        if response.status_code == 200:
            data = response.json()
            reply = data.get("reply", "Samajh nahi aaya bhai.")

            # extra safety: reply length trim
            if len(reply) > 120:
                reply = reply[:120]

            return reply

        else:
            return "Server thoda busy hai bhai."

    except Exception as e:
        return f"Error: {e}"
