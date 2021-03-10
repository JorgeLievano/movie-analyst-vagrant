import os
import subprocess

cwd = os.getcwd()
log_user = os.getlogin()

subprocess.run(['git', 'clone', 'https://gitlab.com/movie-analyst/movie-analyst-api.git'],check=True)
os.chdir('./movie-analyst-api/')
subprocess.run(['npm', 'install'], check=True)
subprocess.run(['pm2', 'start', 'server.js', '--name', 'api'],check=True)
os.chdir(cwd)

subprocess.run(['git', 'clone', 'https://gitlab.com/movie-analyst/movie-analyst-ui.git'],check=True)
os.chdir('./movie-analyst-ui/')
subprocess.run(['npm', 'install'], check=True)
subprocess.run(['pm2', 'start', 'server.js', '--name', 'ui'],check=True)
os.chdir(cwd)

subprocess.run(['pm2', 'save'],check=True)

#subprocess.run(['sudo', 'systemctl', 'restart', f'pm2-{log_user}'],check=True)