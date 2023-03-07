# Python Face Recognition Program
This is a Python program that uses a trained face recognition model to identify faces in images. The program is built using the face_recognition library and Docker containerization.

## Requirements
To run this program, you will need:

- [Docker](https://www.docker.com/) installed on your computer
- Images of persons that the model has been trained on

## To execute the program, follow the steps below:

Step 1: Open the terminal and navigate to the directory where the program files are stored.

Step 2: Run the command docker-compose up --build to build and run the Docker container.
```
docker-compose up --build
```

Step 3: Open the another terminal or command prompt on your computer and enter the following command:

```
docker ps
```

This command will list all the running containers in Docker and display their CONTAINER ID.

Step 4: Once you have copied the CONTAINER ID of the container you want to work with, create a new command by replacing <CONTAINER ID> with the actual CONTAINER ID:

```
docker exec -it <CONTAINER ID> sh
```

This command will start an interactive session with the container you have selected.

Step 5: Once you are inside the container, change the directory to the root folder by typing the following command:

```
cd root
```

Step 6: Copy any image file to the ```input_image``` folder, but make sure that the image belongs to one of the persons listed below, as the face recognition model is being trained for these persons:

['Akshay Kumar',
'Alexandra Daddario',
'Alia Bhatt',
'Amitabh Bachchan',
'Andy Samberg',
'Anushka Sharma',
'Billie Eilish',
'Brad Pitt',
'Camila Cabello',
'Charlize Theron',
'Claire Holt',
'Courtney Cox',
'Dwayne Johnson',
'Elizabeth Olsen',
'Ellen Degeneres',
'Henry Cavill',
'Hrithik Roshan',
'Hugh Jackman',
'Jessica Alba',
'Kashyap',
'Lisa Kudrow',
'Margot Robbie',
'Marmik',
'Natalie Portman',
'Priyanka Chopra',
'Robert Downey Jr',
'Roger Federer',
'Tom Cruise',
'Vijay Deverakonda',
'Virat Kohli',
'Zac Efron']

Step 7: Finally, execute the Python script by running the following command:

```
python predict.py
```

This command will run the script and use the image you copied to the input folder to make a prediction using the face recognition model.

---

# How to install docker and docker compose
Windows Terminal enables multiple tabs (quickly switch between multiple Linux command lines, Windows Command Prompt, PowerShell, Azure CLI, etc), create custom key bindings (shortcut keys for opening or closing tabs, copy+paste, etc.), use the search feature, and custom themes (color schemes, font styles and sizes, background image/blur/transparency).

Install [Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/get-started)

## Docker Installation steps

---

### In Windows Machine

#### Step1: Download Docker Desktop
For windows download [Docker Desktop](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe).

#### Step2: Turn on some optional features on Windows 10
Turn on the Hyper-V, Virtual Machine Platform and Windows Hypervisor Platform in windows machine.

Here's how to turn on or off optional features on Windows 10 using Control Panel:
1. Open Control Panel.
2. Click on Programs.
3. Click the Turn Windows features on or off link.

#### Step3: Download linux distribution
Download linux distribution [Ubuntu 20.04 LTS](https://www.microsoft.com/store/apps/9n6svws3rx71)

For more information check out the [windows subsystem for linux installation guide for windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

#### Step4: Give user-group permission access
In order to install docker in windows you need to give [user-group](https://www.mtgimage.org/add-user-to-docker-users-group-windows-10/) access.

#### Step5: Install Windows Terminal
Windows Terminal enables multiple tabs (quickly switch between multiple Linux command lines, Windows Command Prompt, PowerShell, Azure CLI, etc), create custom key bindings (shortcut keys for opening or closing tabs, copy+paste, etc.), use the search feature, and custom themes (color schemes, font styles and sizes, background image/blur/transparency).

Install [Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/get-started)

---

### Install in Linux Machine

#### Step1: First, update your existing list of packages:

```
sudo apt update
```
Next, install a few prerequisite packages which let apt use packages over HTTPS:
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
Then add the GPG key for the official Docker repository to your system:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
Add the Docker repository to APT sources:
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```
Next, update the package database with the Docker packages from the newly added repo:
```
sudo apt update
```
Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:
```
apt-cache policy docker-ce
```
You’ll see output like this, although the version number for Docker may be different:
```
Output of apt-cache policy docker-ce
docker-ce:
  Installed: (none)
  Candidate: 5:19.03.9~3-0~ubuntu-focal
  Version table:
     5:19.03.9~3-0~ubuntu-focal 500
        500 https://download.docker.com/linux/ubuntu focal/stable amd64 Packages
```
Notice that docker-ce is not installed, but the candidate for installation is from the Docker repository for Ubuntu 20.04 (focal).

Finally, install Docker:
```
sudo apt install docker-ce
```
Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it’s running:
```
sudo service docker start
sudo service docker status
```
The output should be similar to the following, showing that the service is active and running:

Output
```
* Docker is running
```
Installing Docker now gives you not just the Docker service (daemon) but also the docker command line utility, or the Docker client.

#### Step 2: Executing the Docker Command Without Sudo (Optional)
By default, the docker command can only be run the root user or by a user in the docker group, which is automatically created during Docker’s installation process. If you attempt to run the docker command without prefixing it with sudo or without being in the docker group, you’ll get an output like this:

Output
docker: Cannot connect to the Docker daemon. Is the docker daemon running on this host?.
See ```'docker run --help'```.
If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group:
```
sudo usermod -aG docker ${USER}
```
To apply the new group membership, log out of the server and back in, or type the following:
```
su - ${USER}
```
You will be prompted to enter your user’s password to continue.

Confirm that your user is now added to the docker group by typing:
```
id -nG
```
Output
```
vaibhav adm dialout cdrom floppy sudo audio dip video plugdev netdev docker
```
If you need to add a user to the docker group that you’re not logged in as, declare that username explicitly using:

```
sudo usermod -aG docker username
```
#### Step3: Install docker-compose
Docker Compose relies on Docker Engine for any meaningful work, so make sure you have Docker Engine installed either locally or remote, depending on your setup.
```
sudo apt install docker-compose
```
or 
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

