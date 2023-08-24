class Linter:
    def __init__(self):
        self.stack = []
        self.error = None

    # 문법 오류 검사 ⛏ 
    def lint(self, text):

        for index, char in enumerate(text):
            # 문자가 여는 괄호면 스택에 푸시 
            if self.opening_brace(char):
                self.stack.append(char)
            elif self.closing_brace(char):
                # 문자가 닫는 괄호 문자가 최근에 나온 여는 괄호를 닫았다면 
                if self.closes_most_recent_opening_brace(char):
                    # 스택에서 해당 여는 괄호를 팝 
                    self.stack.pop()
                else:
                    # 닫는 괄호 문자가 최근에 나온 여는 괄호를 닫지 않음 
                    self.error = f"Incorrect closing brace: {char} at index {index}"
                    return

        if self.stack:
            # 스택이 비어있지 않는다면  
            # 대응하는 닫는 괄호가 나오지 않음 
            self.error = f"{self.stack[-1]} does not have a closing brace"

    def opening_brace(self, char):
        return char in ["(", "[", "{"]

    def closing_brace(self, char):
        return char in [")", "]", "}"]

    def opening_brace_of(self, char):
        return {")": "(", "]": "[", "}": "{"}[char]

    def most_recent_opening_brace(self):
        return self.stack[-1]

    def closes_most_recent_opening_brace(self, char):
        return self.opening_brace_of(char) == self.most_recent_opening_brace()

    
linter = Linter()
linter.lint("( var x = { y: [1, 2, 3] } ")
print(linter.error)


