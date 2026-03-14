import requests
import urllib.parse

def get_iro_reply(user_text):
    try:
        prompt = "Reply in casual Hinglish like a friendly Indian: " + user_text
        text = urllib.parse.quote(prompt)

        url = f"https://stdgpt.vercel.app/?text={text}"
        response = requests.get(url, timeout=60)

        if response.status_code == 200:
            data = response.json()
            return data.get("reply", "Reply nahi mila AI se.")
        else:
            return "AI server respond nahi kar raha."

    except Exception as e:
        return f"Error: {e}"
