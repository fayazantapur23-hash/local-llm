import openai
openai.api_base = "http://38.128.233.171:8000/v1"
openai.api_key = "not-needed"
res = openai.ChatCompletion.create(
model="openai/gpt-oss-20b",
messages=[{"role": "user", "content": "Explain quantum mechanics"}],
stream=True
)
for chunk in res:
    print(chunk.choices[0].delta.get("content", ""), end="", flush=True)
