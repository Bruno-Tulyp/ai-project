import yaml

class CodeAnalyzer:
    def __init__(self, mode):
        with open('prompts/templates.yaml', 'r') as file:
            self.prompts = yaml.safe_load(file)
        self.mode = mode

    def generate_prompt(self, code_snippet):
        prompt = self.prompts.get(self.mode, {}).get("description", "")
        return f"{prompt}\n\nCode to review:\n{code_snippet}"

    def analyze_code(self, code_snippet, llm_client):
        prompt = self.generate_prompt(code_snippet)
        review = llm_client.run(prompt)
        return review
