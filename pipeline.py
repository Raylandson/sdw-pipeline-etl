import json
import requests

headers = {
    "Authorization": "Bearer YOUR_KEY"
}
url = "https://api.edenai.run/v2/text/generation"


with open("costumers_data.json", "r") as json_file:
    raw_data = json.load(json_file)

data = raw_data.copy()

def generate_ai_news(user):
    payload = {
        "providers": "openai",
        "text": f"És um especialista em marketing bancário, crie uma mensagem única sobre a importância dos investimentos para {user['name']}",
        "temperature": 0.2,
        "max_tokens": 100,
    }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    return result["openai"]["generated_text"] if response.status_code == 200 else ""


for costumer in data["costumers"]:
    new = generate_ai_news(costumer)
    if not new:
        continue
    costumer["news"].append(
        {"id": len(costumer["news"]), "icon": "string", "description": new}
    )


save_data = open("costumers_data.json", "w")
json.dump(data, save_data, indent=6)
save_data.close()


