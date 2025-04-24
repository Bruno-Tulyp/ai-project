import openai
import anthropic
import requests
import yaml

class LLMClient:
    def __init__(self, provider):
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)

        self.provider = provider
        self.api_key = config[provider]['key']
        self.model = config[provider]['model']

    def run(self, prompt):
        if self.provider == "openai":
            return self._call_openai(prompt)
        elif self.provider == "ollama":
            return self._call_ollama(prompt)
        elif self.provider == "anthropic":
            return self._call_claude(prompt)

    def _call_openai(self, prompt):
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(model=self.model, max_tokens=500, messages=[{"role": "user", "content": prompt}])
        return response.choices[0].message.content.strip()

    def _call_ollama(self, prompt):
        url = "http://localhost:11434/api/generate"
        headers = {"Content-Type": "application/json"}
        data = {"model": self.model, "prompt": prompt, "stream": False}
        response = requests.post(url, json=data, headers=headers)
        return response.json().get("response", "").strip()

    def _call_claude(self, prompt):
        client = anthropic.Anthropic(api_key=self.api_key)
        response = client.messages.create(model=self.model, max_tokens=500, messages=[{"role": "user", "content": prompt}])
        return response.content[0].text.strip()
