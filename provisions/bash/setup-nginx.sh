#!/bin/bash
sudo apt-get update
sudo apt-get install -y nginx expect

sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'

ENABLED_UFW=$(expect -c "
set timeout 10

spawn sudo ufw enable

expect \"Command may disrupt existing ssh connections. Proceed with operation \(y\|n\)\?\"
send \"y\r\"
expect eof
")

echo "$ENABLED_UFW"