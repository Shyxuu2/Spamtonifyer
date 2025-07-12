import re
text = "now's your chance"
tokens = re.findall(r"[a-zA-Z0-9']+|[!?;.,]+", text)
print(tokens)  # ['now's', 'your', 'chance']
