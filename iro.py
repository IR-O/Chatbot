import requests

def get_iro_reply(user_text):
    try:
        url = f"https://stdgpt.vercel.app/?text={user_text}"
        response = requests.get(url, timeout=60)

        if response.status_code == 200:
            return response.text
        else:
            return "AI Error: API not responding"

    except Exception as e:
        return f"Error: {e}"
