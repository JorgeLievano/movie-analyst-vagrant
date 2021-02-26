#!/bin/bash
sudo apt-get update
sudo apt-get install mysql-server expect -y
MYSQL_ROOT_PASSWORD="dummie@123"

      SECURE_MYSQL=$(expect -c "

      set timeout 10
      spawn mysql_secure_installation

      expect \"Enter password for user root:\"
      send \"\r\"

      expect \"Change the password for root ?\(Press y\|Y for Yes, any other key for No\) :\"
      send \"y\r\"

      expect \"New password:\"
      send \"$MYSQL_ROOT_PASSWORD\r\"

      expect \"Re-enter new password:\"
      send \"$MYSQL_ROOT_PASSWORD\r\"

      expect \"Do you wish to continue with the password provided?\(Press y\|Y for Yes, any other key for No\) :\"
      send \"y\r\"

      expect \"Remove anonymous users?\(Press y\|Y for Yes, any other key for No\) :\"
      send \"y\r\"

      expect \"Disallow root login remotely?\(Press y\|Y for Yes, any other key for No\) :\"
      send \"n\r\"

      expect \"Remove test database and access to it?\(Press y\|Y for Yes, any other key for No\) :\"
      send \"y\r\"

      expect \"Reload privilege tables now?\(Press y\|Y for Yes, any other key for No\) :\"
      send \"y\r\"

      expect eof
      ")

      echo "$SECURE_MYSQL"
      #mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';"
      mysql -u root -e "CREATE DATABASE movie_db;"
      mysql -u root -psomething -e "CREATE USER 'movieadm'@'localhost' IDENTIFIED BY '$MYSQL_ROOT_PASSWORD';GRANT ALL PRIVILEGES ON movie_db.* TO 'movieadm'@'localhost';"
      mysql -u root -e "FLUSH PRIVILEGES;"

      service mysql restart