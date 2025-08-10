🚀 Setting up vLLM APIs using GPT-OSS 120B Model on Hyperstack Cloud
This guide walks you through setting up a local cloud-based LLM using gpt-oss-120b on Hyperstack Cloud, and accessing it via cURL, Postman, and Python.

- [Prerequisites](#-prerequisites)  
- [1️⃣ Step 1: Deploy VM on Hyperstack](#1️⃣-step-1-deploy-vm-on-hyperstack)  
- [2️⃣ Step 2: Install Python 3.12](#2️⃣-step-2-install-python-312)  
- [3️⃣ Step 3: Create Python Virtual Environment](#3️⃣-step-3-create-python-virtual-environment)  
- [4️⃣ Step 4: Upgrade pip & Install vLLM with GPT-OSS Wheels](#4️⃣-step-4-upgrade-pip--install-vllm-with-gpt-oss-wheels)  
- [5️⃣ Step 5: Start vLLM Server](#5️⃣-step-5-start-vllm-server)  
- [6️⃣ Step 6: Test with cURL & Postman](#6️⃣-step-6-test-with-curl--postman)  
- [7️⃣ Step 7: Test with Python Scripts](#7️⃣-step-7-test-with-python-scripts)  



## ✅ Prerequisites
PuTTY & PuTTYGen → Download Here

Hyperstack Cloud Account with credits → Sign Up

Basic knowledge of SSH, Linux commands, and Python virtual environments.

## 1️⃣ Step 1: Deploy VM on Hyperstack
# 🚀 Deploying gpt-oss:120b on Hyperstack Cloud with Open WebUI

[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-orange?logo=ubuntu)](https://ubuntu.com/)  
[![GPU](https://img.shields.io/badge/GPU-H100-green?logo=nvidia)](https://www.nvidia.com/en-us/data-center/h100/)  
[![Docker](https://img.shields.io/badge/Docker-24.0+-blue?logo=docker)](https://www.docker.com/)  
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)  
[![Hyperstack](https://img.shields.io/badge/Cloud-Hyperstack-purple)](https://console.hyperstack.cloud/)

A complete, step-by-step guide to run **gpt-oss:120b** locally on a Hyperstack VM with **H100 GPU**, using **Docker** & **Open WebUI**.

🔗 **Hyperstack Cloud:** [https://console.hyperstack.cloud/](https://console.hyperstack.cloud/)

---

## 📑 Table of Contents

1. [📋 Prerequisites](#-prerequisites)  
2. [1️⃣ Deploy VM on Hyperstack](#1️⃣-deploy-vm-on-hyperstack)  
3. [2️⃣ Create SSH Key in PuTTYgen](#2️⃣-create-ssh-key-in-puttygen)  
4. [3️⃣ Enable Networking](#3️⃣-enable-networking)  
5. [4️⃣ Connect to VM via PuTTY](#4️⃣-connect-to-vm-via-putty)  

---

## 📋 Prerequisites
- **PuTTY** & **PuTTYgen** installed → [Download Here](https://puttygen.com/download-putty)  
- **Hyperstack Cloud** account with credits  
- Basic terminal knowledge  

---

## 1️⃣ Deploy VM on Hyperstack
1. **Login** → Click **Deploy a New Virtual Machine**  
   ![Deploy VM](https://github.com/user-attachments/assets/386479bc-1b77-49b2-b437-862e8f4444da)

2. **Select Environment:** `default-CANADA-1`  
   ![Environment](https://github.com/user-attachments/assets/375b1192-8151-4785-9ef6-1aba7d987273)

3. **Select OS Image**  
   ![OS Image](https://github.com/user-attachments/assets/641065e6-a9bd-4022-ae74-e77203e226b2)

---

## 2️⃣ Create SSH Key in PuTTYgen
1. Open **PuTTYgen** → Click **Generate**  
2. Copy **Public Key** & Save **Private Key** (`.ppk`)  
   ![Key](https://github.com/user-attachments/assets/8bf89582-52c1-4458-9e93-198688bc6beb)

3. In Hyperstack → **Create New SSH Key**  
4. Paste public key & import  
   ![Import Key](https://github.com/user-attachments/assets/7ac212d4-c774-4ada-9e2b-15421c6c82c0)

---

## 3️⃣ Enable Networking
1. Enable **SSH Access** & **Public IP**  
2. Click **Configure Additional Settings**  
3. Add inbound & outbound rules → Example: Ports `3000-9000`  
   ![Ports](https://github.com/user-attachments/assets/b6f4347f-ab5d-4c9a-a32b-4ad3284c5446)

4. Click **Deploy** → Wait 2–3 minutes for VM  

---

## 4️⃣ Connect to VM via PuTTY
1. Open **PuTTY**  
2. Enter **VM IP & Port**  
3. Go to **Connection → SSH → Auth → Credentials** → Browse `.ppk` file  
4. Connect → Login as `ubuntu`  
   ![PuTTY Login](https://github.com/user-attachments/assets/8fd11636-2569-493a-a348-31305d9a4b3a)

---

## 2️⃣ Step 2: Install Python 3.12
```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev -y

```

---

## 3️⃣ Step 3: Create Python Virtual Environment
```bash
python3.12 -m venv .venv
source .venv/bin/activate

```

---

## 4️⃣ Step 4: Upgrade pip & Install vLLM with GPT-OSS Wheels
```bash
pip install --upgrade pip setuptools wheel

pip install --pre vllm==0.10.1+gptoss \
--extra-index-url https://wheels.vllm.ai/gpt-oss \
--extra-index-url https://download.pytorch.org/whl/nightly/cu128

```

---


## 5️⃣ Step 5: Start vLLM Server
```bash
vllm serve openai/gpt-oss-20b \
--port 8000 \
--gpu-memory-utilization 0.9 \
--max-model-len 8192

```
<img width="1467" height="565" alt="image" src="https://github.com/user-attachments/assets/ef726baf-3469-4a56-971b-40b11d8a140d" />

---


✅ You should see "Started server" in the terminal.

<img width="1048" height="222" alt="image" src="https://github.com/user-attachments/assets/6f435fae-2c95-4106-9c0b-522c286434d6" />

## 6️⃣ Step 6: Test with cURL & Postman

Basic cURL Request:

```bash
curl --location 'http://<VM-IP>:8000/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer not-needed' \
--data '{
"model": "openai/gpt-oss-20b",
"messages": [
{"role": "user", "content": "Explain quantum mechanics"}
],
"max_tokens": 200
}'


```
<img width="1378" height="767" alt="image" src="https://github.com/user-attachments/assets/9996a42b-e2f7-438c-a0a9-bd330c8f16c6" />

Streaming cURL Request:
```bash
curl --location 'http://<VM-IP>:8000/v1/chat/completions' \
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

```
<img width="1422" height="930" alt="image" src="https://github.com/user-attachments/assets/ccf7adaa-f2b8-44f1-b0ed-f3ebfe1eaeac" />

---


## 7️⃣ Step 7: Test with Python Scripts
- [vllm.py](vllmTestFiles/vllm.py)

  <img width="1220" height="880" alt="image" src="https://github.com/user-attachments/assets/2330b034-0e6a-4ac4-b1e1-eff357adcad6" />\

- [vllmStream.py](vllmTestFiles/vllmStream.py)

 <img width="1166" height="867" alt="image" src="https://github.com/user-attachments/assets/f4e5f57c-c371-41ef-98cf-12daed08c866" />

---
