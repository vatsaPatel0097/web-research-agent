from utils.llm import generate

if __name__ == "__main__":
    prompt = "Write 3 benefits of AI in education."
    response = generate(prompt)
    print(response)
