#!/usr/bin/env bash
#A Bash script that sets up your web servers for the deployment of web_static

apt-get -y update
apt-get -y install nginx

ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/releases/test 
mkdir -p /data/web_static/shared

echo "<p>Simple content to test Nginx Configuration</p>" > /data/web_static/releases/test/index.html

if [ -d "/data/web_static/current" ];
then
    echo "path /data/web_static/current exists"
    rm -rf /data/web_static/current;
fi;

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data

sed -i '/listen 80 default_server/a location /hbnb_static/ {alias /data/web_static/current/;}' /etc/nginx/sites-available/default

ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

service nginx restart
