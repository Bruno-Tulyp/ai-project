import argparse
from agent.analyzer import CodeAnalyzer
from agent.llm_interface import LLMClient

def main():
    parser = argparse.ArgumentParser(description="AI Code Review Agent")
    parser.add_argument('--file', required=True, help="Path to the Python code file")
    parser.add_argument('--mode', required=True, choices=['strict', 'mentor', 'test_focus'], help="Review mode")
    parser.add_argument('--provider', required=True, choices=['openai', 'ollama', 'anthropic'], help="LLM provider")

    args = parser.parse_args()

    with open(args.file, 'r') as file:
        code_snippet = file.read()

    llm_client = LLMClient(provider=args.provider)
    analyzer = CodeAnalyzer(mode=args.mode)

    review = analyzer.analyze_code(code_snippet, llm_client)

    with open('reviews/review_output.md', 'w') as review_file:
        review_file.write(review)

    print(f"Review saved to reviews/review_output.md")

if __name__ == "__main__":
    main()
