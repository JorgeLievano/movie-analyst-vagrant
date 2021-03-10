import subprocess

node_version = '14.x'

#setup node
subprocess.run('curl -fsSL https://deb.nodesource.com/setup_%s -o nodesource_setup.sh' %node_version, shell=True, check=True)
subprocess.run('sudo bash nodesource_setup.sh', shell=True, check=True)
subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nodejs'], check=True)
subprocess.run('node -v', shell=True, check=True)
subprocess.run(['sudo', 'apt-get', 'install', '-y', 'build-essential'], check=True)