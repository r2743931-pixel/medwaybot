import requests

TOKEN = "<PUT_YOUR_TOKEN_HERE>"
RENDER_URL = "https://<YOUR_RENDER_SERVICE>.onrender.com"  # آدرس سرویس Render شما
WEBHOOK_URL = f"{RENDER_URL}/webhook"
resp = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}")
print(resp.status_code)
print(resp.text)
