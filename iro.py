import requests
import urllib.parse

def get_iro_reply(user_text):
    try:
        text = urllib.parse.quote(user_text)
        url = f"https://stdgpt.vercel.app/?text={text}"
        response = requests.get(url, timeout=60)

        if response.status_code == 200:
            return response.text
        else:
            return "AI Error: API not responding"

    except Exception as e:
        return f"Error: {e}"
