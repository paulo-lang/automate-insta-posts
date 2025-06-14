import helpers
from modules.AITools import chatgpt

print("Digite o prompt para criar seu post no Instagram:")
prompt = input()

chatgpt.getChatGPTImage(prompt)


