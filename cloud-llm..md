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
6. [5️⃣ Install Dependencies](#5️⃣-install-dependencies)
7. [6️⃣ Verify GPU](#6️⃣-verify-gpu)
8. [7️⃣ Install Docker & NVIDIA Toolkit](#7️⃣-install-docker--nvidia-toolkit)
9. [8️⃣ Setup Persistent Storage](#8️⃣-setup-persistent-storage)
10. [9️⃣ Install Open WebUI](#9️⃣-install-open-webui)
11. [🔟 Access WebUI](#-access-webui)
12. [🎉 Performance Metrics](#-performance-metrics)
13. [⚡ Troubleshooting](#-troubleshooting)

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
3. Go to **SSH → Auth** → Browse `.ppk` file
4. Connect → Login as `ubuntu`  
   ![PuTTY Login](https://github.com/user-attachments/assets/8fd11636-2569-493a-a348-31305d9a4b3a)

---

## 5️⃣ Install Dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget unzip git build-essential nano
clear
sudo reboot

```
Reconnect after reboot.

---

## 6️⃣ Verify GPU

```bash
nvidia-smi
```
✔ You should see H100 GPU listed.

## 7️⃣ Install Docker & NVIDIA Toolkit

```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker

distribution=$(. /etc/os-release; echo $ID$VERSION_ID)

curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
| sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg

curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list \
| sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#' \
| sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt update
sudo apt install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

Test GPU in Docker:

```bash
docker run --rm --gpus all nvidia/cuda:12.2.0-base-ubuntu22.04 nvidia-smi
```

---


## 8️⃣ Setup Persistent Storage

```bash
sudo mkdir -p /ephemeral/ollama
sudo chown -R $USER:$USER /ephemeral/ollama
```

---


## 9️⃣ Install Open WebUI

```bash
git clone https://github.com/open-webui/open-webui.git
cd open-webui
nano docker-compose.yaml
docker compose up -d
'''

Check logs:

```bash
docker logs -f open-webui
docker logs -f ollama
```

Pull model:

```bash
docker exec -it ollama ollama pull gpt-oss:120b
```

---


## 🔟 Access WebUI
Direct: http://<your-vm-ip>:3000

<img width="1386" height="721" alt="image" src="https://github.com/user-attachments/assets/dcad7f39-ab47-45f9-a726-2a1bbd5cc8a9" />

🚀 Your local LLM — gpt-oss:120b — is up and running!

<img width="1510" height="797" alt="image" src="https://github.com/user-attachments/assets/0a376b73-7a6f-4484-9a1c-e96b5fb84d97" />

Ngrok (if no public IP):

```bash
sudo snap install ngrok
ngrok config add-authtoken <your-token>
ngrok http 3000
```

<img width="956" height="297" alt="image" src="https://github.com/user-attachments/assets/a43c31be-1002-4add-93e4-6cda938a8d17" />

🎉 It’s live! The application is now publicly accessible — share it with friends and family to help test and gather feedback.

<img width="1525" height="826" alt="image" src="https://github.com/user-attachments/assets/606c6038-c083-43b0-aa5d-c8f1a1797536" />


---


## 🎉 Performance Metrics
Performace matrics , after entering prompt 

<img width="1568" height="773" alt="image" src="https://github.com/user-attachments/assets/f384035a-bfcb-4268-97d7-528c40a81742" />

<img width="1507" height="597" alt="image" src="https://github.com/user-attachments/assets/cfa5b478-4577-4179-a05c-b1d3e5e8abcf" />

---


## ⚡ Troubleshooting
Issue	Possible Cause	Solution
Permission denied when running Docker	User not in docker group	Run: sudo usermod -aG docker $USER && newgrp docker
nvidia-ctk: command not found	NVIDIA Container Toolkit not installed correctly	Re-run NVIDIA Toolkit install steps in Section 7
nvidia-smi not showing GPU	NVIDIA drivers missing or VM not GPU-enabled	Check VM specs in Hyperstack → redeploy with GPU
docker: Error response from daemon: could not select device driver "" with capabilities: [[gpu]]	Docker not configured with NVIDIA runtime	Run: sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker
Connection timed out in PuTTY	Wrong IP or firewall rules not set	Verify VM public IP and inbound rules for port 22
WebUI not loading	Port not open or container stopped	Check with: docker ps and ensure port 3000 is in inbound rules

---


## 💡 Tip: After changes, restart services:

```bash
sudo systemctl restart docker
docker compose restart
```

---
