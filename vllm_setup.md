Step 2: Install Python 3.12

sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev -y

Step 3: Create Virtual Environment

python3.12 -m venv .venv
source .venv/bin/activate

Step 4: Upgrade pip, setuptools, wheel

pip install --upgrade pip setuptools wheel

Step 5: Install vLLM with GPT-OSS Wheels

pip install --pre vllm==0.10.1+gptoss \
--extra-index-url https://wheels.vllm.ai/gpt-oss \
--extra-index-url https://download.pytorch.org/whl/nightly/cu128

vllm serve openai/gpt-oss-20b \
--port 8000 \
--gpu-memory-utilization 0.9 \
--max-model-len 8192


<img width="1467" height="565" alt="image" src="https://github.com/user-attachments/assets/ef726baf-3469-4a56-971b-40b11d8a140d" />

Make sure you see, Started server in terminal

<img width="1048" height="222" alt="image" src="https://github.com/user-attachments/assets/6f435fae-2c95-4106-9c0b-522c286434d6" />

Copy the curl command test it in postman

curl --location 'http://38.128.233.171:8000/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer not-needed' \
--data '{
"model": "openai/gpt-oss-20b",
"messages": [
{"role": "user", "content": "Explain quantum mechanics"}
],
"max_tokens": 200
}'

<img width="1378" height="767" alt="image" src="https://github.com/user-attachments/assets/9996a42b-e2f7-438c-a0a9-bd330c8f16c6" />



For stareming use below curl command , you will get result in chunk

curl --location 'http://38.128.233.171:8000/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer not-needed' \
--data '{
"model": "openai/gpt-oss-20b",
"messages": [
{"role": "user", "content": "Explain quantum mechanics"}
],
"max_tokens": 200,
"stream": true
}'


<img width="1422" height="930" alt="image" src="https://github.com/user-attachments/assets/ccf7adaa-f2b8-44f1-b0ed-f3ebfe1eaeac" />

Refer python program as well to connect apis

<img width="1220" height="880" alt="image" src="https://github.com/user-attachments/assets/2330b034-0e6a-4ac4-b1e1-eff357adcad6" />

for stream

<img width="1166" height="867" alt="image" src="https://github.com/user-attachments/assets/f4e5f57c-c371-41ef-98cf-12daed08c866" />



