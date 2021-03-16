import subprocess
import pexpect
import os
import shutil

log_user = os.getlogin()
os.chdir(f'/home/{log_user}')
api_domain = 'api.movieanalyst.com'
ui_domain = 'movieanalyst.com'

subprocess.run(['sudo', 'apt-get', 'update'], check=True)
subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nginx'], check=True)
subprocess.run(['sudo', 'ufw', 'allow', 'OpenSSH',], check=True)
subprocess.run(['sudo', 'ufw', 'allow', 'Nginx HTTP',], check=True)

ufwchild = pexpect.spawn('sudo ufw enable')
ufwchild.expect('Command may disrupt existing ssh connections. Proceed with operation \(y\|n\)\?')
ufwchild.sendline('y')
ufwchild.expect(pexpect.EOF)

userid = os.getuid()
groupid = os.getgid()

os.makedirs(f'/var/www/{api_domain}/html')
os.chown(f'/var/www/{api_domain}/html',userid,groupid)
os.chmod(f'/var/www/{api_domain}', 755)
shutil.copy('./nginx-sources/index.html', f'/var/www/{api_domain}/html/index.html')
shutil.copy(f'./nginx-sources/{api_domain}', '/etc/nginx/sites-available/')
os.symlink(f'/etc/nginx/sites-available/{api_domain}',f'/etc/nginx/sites-enabled/{api_domain}')

os.makedirs(f'/var/www/{ui_domain}/html')
os.chown(f'/var/www/{ui_domain}/html',userid,groupid)
os.chmod(f'/var/www/{ui_domain}', 755)
shutil.copy('./nginx-sources/index.html', f'/var/www/{ui_domain}/html/index.html')
shutil.copy(f'./nginx-sources/{ui_domain}', f'/etc/nginx/sites-available/')
os.symlink(f'/etc/nginx/sites-available/{ui_domain}',f'/etc/nginx/sites-enabled/{ui_domain}')

subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'], check=True)