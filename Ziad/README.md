Welcome to my README!
----------------------


This is mainly resources that I created to implement and setup the MEC server for the waglle-sensor project. There are also usefull links and courses 
that helped me to figure out some tasks.
<hr>

<b>Set up SSH server:</b> 

<sub>Install ssh server</sub>
```
sudo apt-get install openssh-server

sudo apt update

sudo service ssh status

sudo service ssh start or sudo systemctl start ssh
```


<sub>Create Private Key</sub>

```
ssh-keygen -t rsa -b 4096

cd  .ssh/

cp id_rsa.pub authorized_keys

mkdir .ssh                 // on the server

scp authorized_keys  username@ip_address:/home/username/.ssh

chmod 700 ~/.ssh          // on the server

chmod 600~/.ssh           // on the server
```


<b>Set up Docker</b>

<sub>Update the apt package index and install packages to allow apt to use a repository over HTTPS:</sub>
```
 sudo apt-get update
 sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

<sub>Add Docker’s official GPG key:</sub>
```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
<sub>use the following command to set up the repository</sub>
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
<sub>Install the Docker Engine</sub>
<sub>Update the apt package index, and install the latest version of Docker Engine, containerd, and Docker Compose, or go to the next step to install a specific version:</sub>

```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

<sub>Verify that Docker Engine is installed correctly by running the hello-world image.</sub>
```
 sudo docker run hello-world
```
<sub>This command downloads a test image and runs it in a container. When the container runs, it prints a message and exits.</sub>


<b>Set up Kubectl</b>

<sub>Download the latest release with the command:</sub>

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```
<sub>Validate the binary</sub>
<sub>Download the kubectl checksum file:</sub>
```
curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
```
<sub>Validate the kubectl binary against the checksum file:</sub>
```
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
```
<sub>If valid, the output is:</sub>
```
kubectl: OK
```
<sub>Install kubectl</sub>
```
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```
<sub>test to ensure the version you installed is up-to-date</sub>
```
kubectl version --client
```

<b>Set up Apache server</b>

<sub>Install Apache</sub>
```
Sudo apt update

Sudo apt-get install apache2

Sudo /etc/init.d/apache2 status
```
<sub>To the index.html file: /var/www/html </sub>

<sub>To access the website: https://localhost </sub>

<sub>For Debugging: https://upcloud.com/resources/tutorials/fix-common-problems-apache2</sub>

<b>Set up HTTP server</b>

<sub>OPTION 1:</sub>
```
Python3 -m http.server 9000 -b IP_ADDRESS
```
<sub>OPTION 2:</sub>
```
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(200)
       self.send_header("Content-type", "text/html")
       self.end_headers()
       self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
       self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
       self.wfile.write(bytes("<body>", "utf-8"))
       self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
       self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":       
   webServer = HTTPServer((hostName, serverPort), MyServer)
   print("Server started http://%s:%s" % (hostName, serverPort))

   try:
       webServer.serve_forever()
   except KeyboardInterrupt:
       pass

   webServer.server_close()
   print("Server stopped.")
```
<sub>
  Run code using: python main.py
 </sub>
 
 <br>
<sub>
  Access the server from: http://IP_ADDRESS:PORT_NO
</sub>
<br>


<br>
<b>Set up K3D</b>
<br>
<sub>Run the script using curl</sub>
<br>
<br>


```
curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
```
