#!/usr/bin/env bash
#  Prepare your web servers

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Holberton School" > /data/web_static/releases/test/index.html
sed -i '21i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data
service nginx restart
