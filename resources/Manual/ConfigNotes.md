## Notice about config file
Please replace the value in "<>" with your own values, since JSON file does not allow comments.

## Notice about caddyfile and naiveproxy
In server side, naiveproxy relies on a caddy server with forward proxy plugin.
For more details please refer their [official documentation](https://github.com/klzgrad/naiveproxy)
since Caddy's breaking change, we need to convert it to a json file
to run caddy with caddyfile format, use adapter
```shell
  caddy adapt --config <your_caddy_file> --adapter caddyfile
```
And you should wait before caddy is ready to accept income connections, and you may not get output notice when it is ready.

## Note about automation of the certs management
We use [acme.sh](https://github.com/acmesh-official/acme.sh) to manage the certs renewal and installation after renewal.
We also use nginx to do acme challenge, if you are using apache or prefer other methods please refer to their manual.
We also write a corresponding systemd timer configuration to automate the renewal process, if you prefer `crontab` or other approaches, just change it accordingly.
Related file: `CertsRenewal.sh`, `acme.sh.timer`, `acme.sh.service`
Because we created a new user `acme.sh` and its home directory, please take care of user permission stuff when you are using it.
And remember to give user acme.sh the permission to restart nginx, change sudoer file, add that
```shell
acme.sh ALL=(ALL) NOPASSWD: /bin/systemctl restart nginx
```

## For the deployment of Tor Obfs4 Bridge in server side, please refer to the official documentation
[Installation](https://community.torproject.org/relay/setup/bridge/debian-ubuntu/)
[Configuration](https://community.torproject.org/relay/setup/bridge/post-install/)
NOTICE:
1. Use your TOR server fingerprint rather than the bridge fingerprint when you try to add your bridge to your TOR browser client. 
2. If you don't want to make your bridge available to the public, please add these lines to your torrc file
    ```shell
      PublishServerDescriptor 0
    ```
3. You may need to use `setcap` in package `libcap` to grant obfs4 to establish connection on port number lower than 1024
You may need to use `iptables` to redirect traffic to the port number that obfs4 is listening on, since obfs4 is running as a user process, it cannot listen on port number lower than 1024.
```shell
    sudo setcap cap_net_bind_service=+ep /usr/bin/obfs4proxy
```
4. When you want to add Tor's package source to your apt source list, please change your version name accordingly.
    For example a source for Debian "Bulleye" will not support a server which runs Debian "Bookworm".

## Notice about fallback server
The upstream fallback server address should be correctly configured in the proxy server configuration file or the proxy server cannot work correctly.
Please refer to the official documentation of the HTTP server (Apache, Nginx) you are using. 
And don't forget to accordingly change the SSL path and the `CertsRenewal.sh` and give enough permission.

