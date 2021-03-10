#!/bin/bash
echo ">>>>>> Start api provisioning script <<<<<<"
">>>>>> Start node setup <<<<<<"
python3 setup-node.py
echo ">>>>>> Start pm2 setup <<<<<<"
python3 setup-pm2.py
echo "End api provisioning script <<<<<<"