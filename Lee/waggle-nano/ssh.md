### Set up SSH public key authentication to connect to a remote system

#### Getting a List of SSH Commands and Syntax
```ssh```

### Set up public key authentication using SSH on a Linux or macOS computer
To generate RSA keys, on the command line, enter:  
```ssh-keygen -t rsa```

### Use SFTP or SCP to copy the public key file (for example, ~/.ssh/id_rsa.pub) to your account on the remote system
```scp ~/.ssh/id_rsa.pub waggle@IP-Address```

### SSH Access
```ssh waggle@10.0.0.151```


## After re-flashed June 28th
### SSH Access
```ssh-keygen -R 10.0.0.151```

### Install the same docker file from https://hub.docker.com/r/waggle/gpu-stress-test/tags
```docker pull waggle/gpu-stress-test:1.0.1```

### You won't see the any output on your terminal,
```sudo docker run -it --rm --runtime nvidia --network host waggle/gpu-stress-test:1.0.1 -m 2```


### Python version update
```apt install -y gcc g++ zlib1g-dev autoconf automake make m4 libpython3.6-dev python3-dev wget```
```update-alternatives --install /usr/bin/python python /usr/bin/python3 1```
