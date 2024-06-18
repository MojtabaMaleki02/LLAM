import json
from llamaapi import LlamaAPI

llama = LlamaAPI('LL-EbDZPWue1gk4Wr26VPHCzkiYOMnq1Xuu9HELZmO8pK7as8jWJWZFHieRtGStf7m7')

user_input = input("Enter your message: ")

api_request_json = {
  "model": "llama3-70b",
  "messages": [
    {"role": "system", "content": "You are a llama assistant that talks like a llama, starting every word with 'll'."},
    {"role": "user", "content": user_input},
  ]
}

try:
    response = llama.run(api_request_json)
    print(response.json()["choices"][0]["message"]["content"])
except Exception as e:
    print("Error:", e)
