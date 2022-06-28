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

### Note: UPDATED!!!!! SSH Access
```ssh-keygen -R 10.0.0.151```
