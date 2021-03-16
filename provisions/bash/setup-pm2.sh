#!/bin/bash
sudo npm install pm2@latest -g
sudo pm2 startup systemd
sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u $USER --hp /home/$USER
sudo systemctl start pm2-$USER