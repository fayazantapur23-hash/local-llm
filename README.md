# 🚀 Setting up Local LLM using **gpt-oss-20b** — Step-by-Step Guide

This guide walks you through setting up **gpt-oss-20b** locally using [Ollama](https://ollama.com/) with a nice **Web UI** for easy interaction.

---

## 📑 Table of Contents
1. [📋 Prerequisites](#-prerequisites)
2. [1️⃣ Install Ollama](#1️⃣-install-ollama)
3. [2️⃣ Download the gpt-oss-20b Model](#2️⃣-download-the-gpt-oss-20b-model)
4. [3️⃣ Start Inferencing](#3️⃣-start-inferencing)
5. [4️⃣ Install Open WebUI (Optional but Recommended)](#4️⃣-install-open-webui-optional-but-recommended)
6. [5️⃣ Access the Web UI](#5️⃣-access-the-web-ui)
7. [6️⃣ Make it Public with Ngrok](#6️⃣-make-it-public-with-ngrok)
8. [🎯 You’re All Set!](#-youre-all-set)

---

## 📋 Prerequisites
- 🐍 **Python** installed  
- 🌐 Stable internet connection (model size is ~20GB)  
- 💾 Enough disk space (**25GB+ free**)

---

## 1️⃣ Install Ollama

📥 **Download & Install** Ollama:  
[🔗 Ollama Download Page](https://ollama.com/download)  
(Installation is straightforward — just follow the installer.)

---

## 2️⃣ Download the gpt-oss-20b Model

Run in your terminal:

```bash
ollama pull gpt-oss:20b
``` 
📦 Model size: ~20GB

---

## 3️⃣ Start Inferencing

Once the download is complete, you can start inferencing directly in Ollama.

<img width="992" height="782" alt="image" src="https://github.com/user-attachments/assets/807b3143-8bf6-40a5-b7ec-3ff4f133c681" />

---


## 4️⃣ Install Open WebUI (Optional but Recommended)

For a better UI experience, install Open WebUI:

```bash
pip install open-webui
open-webui serve
```

---


## 5️⃣ Access the Web UI

Once the server starts, open:

```bash
http://localhost:8080/
``` 

Sign up (first-time use)

<img width="797" height="431" alt="image" src="https://github.com/user-attachments/assets/f1648fc8-8eb8-4db5-b971-ce343a68f358" />

Start chatting with your local LLM

✅ Local LLM is now up & running 🎉

<img width="1658" height="815" alt="image" src="https://github.com/user-attachments/assets/31936bc6-0f78-4a06-983c-16441f65c19a" />

---


## 6️⃣ Make it Public with Ngrok

If you want to share your LLM with others over the internet:

📥 Download Ngrok:

🔗 Ngrok Download for Windows

Unzip the file and open CMD in that folder.

Authenticate Ngrok:

```bash
ngrok config add-authtoken <YOUR_AUTH_TOKEN>
``` 

Expose your Web UI:

```bash
ngrok http 8080
```

<img width="1173" height="688" alt="image" src="https://github.com/user-attachments/assets/b75ffc3e-6e53-4f8e-b986-faaee39566a0" />

You’ll get a public URL like:

```bash
https://4210cddf4e9f.ngrok-free.app/
```

🎯 You’re All Set!

You now have gpt-oss-20b running locally with a nice web interface, and optionally shared online with Ngrok.

Enjoy your private AI assistant! 🤖

<img width="1603" height="832" alt="image" src="https://github.com/user-attachments/assets/79de572e-1b86-4429-905c-cd66b7461711" />
