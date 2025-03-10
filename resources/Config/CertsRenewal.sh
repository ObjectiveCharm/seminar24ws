#!/bin/bash
/home/acme.sh/.acme.sh/acme.sh --register-account -m $MY_EMAIL
# Issue Certificates
/home/acme.sh/.acme.sh/acme.sh --server letsencrypt --renew --issue --nginx  -d "<your_domain>" -d "<your_www_domain_with_same_name>" --keylength ec-256
# Install Certificates for nginx
/home/acme.sh/.acme.sh/acme.sh --install-cert -d adultlily.com \
--key-file       /var/www/keys/key.pem  \
--cert-file      /var/www/certs/cert.pem \
--fullchain-file /var/www/fullchain-files/fullchain.pem \
--reloadcmd     "sudo systemctl restart nginx"