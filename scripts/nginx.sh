
#!/usr/bin/bash

sudo systemctl daemon-reload
sudo rm -rf /etc/nginx/sites-enabled/*

sudo cp /home/ubuntu/fundii_backend/nginx/nginx.conf /etc/nginx/sites-available/fundii_backend
sudo ln -s /etc/nginx/sites-available/fundii_backend /etc/nginx/sites-enabled/
#sudo ln -s /etc/nginx/sites-available/blog /etc/nginx/sites-enabled
#sudo nginx -t
sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx