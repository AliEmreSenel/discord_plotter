import os
import io
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

def send_plot(figure, description="Here is your plot"):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    
    if not webhook_url:
        raise ValueError("Environment variable 'DISCORD_WEBHOOK_URL' is not set.")

    buffer = io.BytesIO()
    figure.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)

    payload = {
        "content": description
    }
    
    files = {
        "file": ("plot.png", buffer, "image/png")
    }

    try:
        response = requests.post(webhook_url, data=payload, files=files)
        response.raise_for_status()
        print(f"Successfully sent plot to Discord. Status Code: {response.status_code}")
    finally:
        buffer.close()
