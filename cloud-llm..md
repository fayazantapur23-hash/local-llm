Setting up cloud local llm using gpt-oss 120b model, https://console.hyperstack.cloud/

Pre - Requisite

On your local make sure you have puttygen and putty downloaded & install https://puttygen.com/download-putty

Signup and some credits in hyperstack cloud 

create and deploy vm H100 GPU , as you can use any vm since its cost is less for experiment we can use it 

Click  -> Deploy a new Virtual Machine

<img width="428" height="403" alt="image" src="https://github.com/user-attachments/assets/386479bc-1b77-49b2-b437-862e8f4444da" />

Select default environment  -> default-CANADA-1

<img width="1530" height="405" alt="image" src="https://github.com/user-attachments/assets/375b1192-8151-4785-9ef6-1aba7d987273" />

Select OS Image

<img width="892" height="427" alt="image" src="https://github.com/user-attachments/assets/641065e6-a9bd-4022-ae74-e77203e226b2" />

In you local Open puttyGen -> Generate - > Copy generated key -> Save Private Key(give any name)

Click Create  new SSH key 

<img width="272" height="71" alt="image" src="https://github.com/user-attachments/assets/8bf89582-52c1-4458-9e93-198688bc6beb" />

After clicking you will see below screen , select environment add name add the generated key from puttyGen -> click import

<img width="891" height="893" alt="image" src="https://github.com/user-attachments/assets/7ac212d4-c774-4ada-9e2b-15421c6c82c0" />

You will see below message after key is added

<img width="487" height="145" alt="image" src="https://github.com/user-attachments/assets/1bb5b3dd-c3c5-49fe-bf28-ebb19e318453" />

Enable SSH Access & Public IP Address

<img width="1036" height="361" alt="image" src="https://github.com/user-attachments/assets/69a07bc7-6ecc-494c-b915-4c4e62bea8ff" />

Click on configure additional settings

<img width="1567" height="122" alt="image" src="https://github.com/user-attachments/assets/633784da-d77d-472f-a6c5-166a90c7618c" />

Add Inbound & Outbound rules

<img width="482" height="362" alt="image" src="https://github.com/user-attachments/assets/65dbf962-7faa-4874-82f7-1462cb27ee0d" />

Enter port range define what you want as i am entering 3000-9000 for both

<img width="1505" height="667" alt="image" src="https://github.com/user-attachments/assets/b6f4347f-ab5d-4c9a-a32b-4ad3284c5446" />

<img width="1557" height="647" alt="image" src="https://github.com/user-attachments/assets/6386571b-94a6-496a-a97d-c3305ac3d5c7" />

Final setp click deploy ,it will take 2 to 3 minutes & your VM will be up and running 

<img width="1500" height="137" alt="image" src="https://github.com/user-attachments/assets/addbff6b-fbd4-4151-9c33-d1b8c3f903bc" />

Here you go!

<img width="1530" height="847" alt="image" src="https://github.com/user-attachments/assets/fec60b19-d821-49d5-aa30-c5e6646b189b" />

Open putty add vm ip & port

<img width="595" height="528" alt="image" src="https://github.com/user-attachments/assets/593521d9-c813-4924-9b1d-741b3f9a77d0" />

click 
<img width="588" height="533" alt="image" src="https://github.com/user-attachments/assets/e68753fd-f8a0-4531-982d-7110c8e26fac" />

click browse , select the file location where you save private key in the initial setp , click open terminal will be displayed 

Login as ubuntu and your terminal is connected 

<img width="772" height="681" alt="image" src="https://github.com/user-attachments/assets/8fd11636-2569-493a-a348-31305d9a4b3a" />

Add dependencies

sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget unzip git build-essential nano
clear
sudo reboot 

wait for couple of minutes & again open termial using above steps

nvidia-smi

<img width="916" height="455" alt="image" src="https://github.com/user-attachments/assets/a17906d0-6e81-4322-b455-36bfc273e9b4" />

You should see your H100 GPU listed.

Install docker 

curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker

Install NVIDIA Container Toolkit

distribution=$(. /etc/os-release; echo $ID$VERSION_ID)

curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg

curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list


sudo apt update
sudo apt install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

Test GPU inside Docker:
docker run --rm --gpus all nvidia/cuda:12.2.0-base-ubuntu22.04 nvidia-smi

Prepare Persistent Storage for Models
sudo mkdir -p /ephemeral/ollama
sudo chown -R $USER:$USER /ephemeral/ollama

Get Open WebUI Repo
git clone https://github.com/open-webui/open-webui.git
cd open-webui

Create docker-compose.yaml
Replace the existing file with this fixed one:
yaml	

nano docker-compose.yaml

Launch Services
docker compose up -d

docker ps

Check logs:

docker logs -f open-webui
docker logs -f ollama

docker exec -it ollama ollama pull gpt-oss:120b

Access WebUI
•	Direct IP: http://<your-vm-ip>:3000

<img width="1386" height="721" alt="image" src="https://github.com/user-attachments/assets/dcad7f39-ab47-45f9-a726-2a1bbd5cc8a9" />

your local llm gpt-oss:120b is running 

<img width="1510" height="797" alt="image" src="https://github.com/user-attachments/assets/0a376b73-7a6f-4484-9a1c-e96b5fb84d97" />

•	ngrok (if no public IP):
bash
CopyEdit
sudo snap install ngrok
ngrok config add-authtoken <your-token>
ngrok http 3000

<img width="956" height="297" alt="image" src="https://github.com/user-attachments/assets/a43c31be-1002-4add-93e4-6cda938a8d17" />

yahoooo its up publically share with your friends and family , for testiing

<img width="1525" height="826" alt="image" src="https://github.com/user-attachments/assets/606c6038-c083-43b0-aa5d-c8f1a1797536" />

Performace matrics , after entering prompt 

<img width="1568" height="773" alt="image" src="https://github.com/user-attachments/assets/f384035a-bfcb-4268-97d7-528c40a81742" />

<img width="1507" height="597" alt="image" src="https://github.com/user-attachments/assets/cfa5b478-4577-4179-a05c-b1d3e5e8abcf" />

