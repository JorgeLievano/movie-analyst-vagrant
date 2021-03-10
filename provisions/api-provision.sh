#!/bin/bash
echo ">>>>>> Start api provisioning script <<<<<<"
echo ">>>>>> Start nginx setup <<<<<<"
sudo python3 setup-nginx.py
echo ">>>>>> Start node setup <<<<<<"
python3 setup-node.py
echo ">>>>>> Start pm2 setup <<<<<<"
python3 setup-pm2.py
echo ">>>>>> Start node apps <<<<<<"
python3 setup-nodeapps.py
echo ">>>>>> End api provisioning script <<<<<<"