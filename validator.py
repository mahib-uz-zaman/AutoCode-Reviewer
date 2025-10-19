import ast

class CodeValidator:
    def check_syntax(self, code):
        try:
            ast.parse(code)
            return "Syntax has no error!"
        except SyntaxError as e:
            return f"Syntax Error: {e}"

    def run_code(self, code):
        try:
            exec(code, {})
            return "Code ran successfully!"
        except Exception as e:
            return f"Runtime Error: {e}"
