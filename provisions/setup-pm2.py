import os
import subprocess

#setup pm2
subprocess.run(['npm', 'install', 'pm2@latest', '-g'], check=True)
subprocess.run(['pm2', 'startup', 'systemd'], check=True)
log_user = os.getlogin()
#print(f'>>>>>> {log_user} <<<<<<')
subprocess.run(f'sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u {log_user} --hp /home/{log_user}', shell=True, check=True)
subprocess.run(['sudo','systemctl', 'start', f'pm2-{log_user}'])