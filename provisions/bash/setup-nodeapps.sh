#!/bin/bash

while getopts g:r:f:n:d: flag
do
    case "${flag}" in
        # git url to clone 
        g) giturl=${OPTARG};;
        # root path of the app
        r) rootpath=${OPTARG};;
        # name of the main file
        f) filename=${OPTARG};;
        # name for the app process
        n) name=${OPTARG};;
        # domain name
        d) domainname=${OPTARG};;
    esac
done

git clone $giturl
cd $rootpath
npm install
pm2 start $filename --name $name
pm2 save

cd ..
sudo mkdir -p "/var/www/$domainname/html"
sudo chown -R $USER:$USER "/var/www/$domainname/html"
sudo chmod -R 755 "/var/www/$domainname"
sudo cp "./nginx-sources/index.html" "/var/www/$domainname/html/index.html"
sudo cp "./nginx-sources/$domainname" "/etc/nginx/sites-available/"
sudo ln -s "/etc/nginx/sites-available/$domainname" "/etc/nginx/sites-enabled/$domainname"
