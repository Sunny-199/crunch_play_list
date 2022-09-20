<VirtualHost *:80>
ServerAdmin webmaster@example.com
DocumentRoot /home/ec2-user/crunchplaylistproject
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
Alias /static /home/ec2-user/crunchplaylistproject/static
<Directory /home/ec2-user/crunchplaylistproject/static>
Require all granted
</Directory>
<Directory /home/ec2-user/crunchplaylistproject/playlistcrunch>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
WSGIDaemonProcess playlistcrunch python-path=/home/ec2-user/crunchplaylistproject/playlistcrunch python-home=/home/ec2-user/crunchplaylistproject/env
WSGIProcessGroup playlistcrunch
WSGIScriptAlias / /home/ec2-user/crunchplaylistproject/playlistcrunch/playlistcrunch/wsgi.py
</VirtualHost>