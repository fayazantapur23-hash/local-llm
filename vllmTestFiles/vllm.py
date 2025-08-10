import openai
openai.api_base = "http://38.128.233.171:8000/v1"
openai.api_key = "sk-fake" # Not used in vLLM
res = openai.ChatCompletion.create(
model="openai/gpt-oss-20b",
messages=[{"role": "user", "content": "Explain quantum mechanics"}]
)
print(res.choices[0].message["content"])
