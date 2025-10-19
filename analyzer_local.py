import subprocess

class CodeAnalyzer:
    def analyze_code(self, code):
        prompt = f"""
You are an expert AI Python code reviewer.
Carefully analyze the provided code for logic correctness, performance efficiency, readability, and potential bugs.
Then respond with:
1. A list of issues and suggested improvements.
2. A revised, improved version of the code that implements those improvements while preserving its original functionality.

Code:
{code}
"""
        # Run local Mistral model via Ollama
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            text=True
        )
        return result.stdout
