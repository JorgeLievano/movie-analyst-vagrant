#import submodules
import pexpect
import subprocess
import os
dummiepasswd = 'Dummie@123'

# install mysql-server
subprocess.run(['sudo', 'apt-get', 'update'], check=True)
subprocess.run(['sudo', 'apt-get', 'install', '-y', 'mysql-server','git'],check=True)
# mysql secure setup
mysqlchild = pexpect.spawn('sudo mysql_secure_installation')
mysqlchild.expect('Press y|Y for Yes, any other key for No:')
mysqlchild.sendline('N')
mysqlchild.expect('New password:')
mysqlchild.sendline(dummiepasswd)
mysqlchild.expect('Re-enter new password:')
mysqlchild.sendline(dummiepasswd)
mysqlchild.expect('Remove anonymous users\? \(Press y\|Y for Yes, any other key for No\) :')
mysqlchild.sendline('Y')
mysqlchild.expect('Disallow root login remotely\? \(Press y\|Y for Yes, any other key for No\) :')
mysqlchild.sendline('N')
mysqlchild.expect('Remove test database and access to it\? \(Press y\|Y for Yes, any other key for No\) :')
mysqlchild.sendline('Y')
mysqlchild.expect('Reload privilege tables now\? \(Press y\|Y for Yes, any other key for No\) :')
mysqlchild.sendline('Y')
mysqlchild.expect(pexpect.EOF,timeout=10)

# create database and user with priviliges
dbname= 'movie_db'
username= 'movieadm'
host= 'localhost'

subprocess.run(['mysql', '-u', 'root', '-e', 'CREATE DATABASE %s;' %dbname], check=True)
subprocess.run(['mysql', '-u', 'root', '-psomething', '-e', 'CREATE USER %s@%s IDENTIFIED BY \'%s\';GRANT ALL PRIVILEGES ON %s.* TO %s@%s;' %(username,host,dummiepasswd,dbname,username,host)],check=True)
subprocess.run(['mysql', '-u', 'root', '-e', 'FLUSH PRIVILEGES;'],check=True)
# restart mysql service to commit changes
subprocess.run(['service', 'mysql', 'restart'], check=True)

#clone database repository
subprocess.run(['git','clone','https://gitlab.com/movie-analyst/movie-analyst-database.git'],check=True)
#create tables and insert data
os.chdir('./movie-analyst-database/')
subprocess.run('sudo mysql --user=%s  --password=%s < table_creation_and_inserts.sql' %(username,dummiepasswd),check=True, shell=True)