# get pem
```openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem```
# Update packages.
```sudo apt-get update```
# Install nodejs.
```
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
```
# Install pip, venv, and nginx.
```sudo apt-get -y install python3.10-pip python3.10-venv nginx```
# Create a directory for the app.
```
mkdir hello_world
cd hello_world
```
# Create and activate the virtualenv.
```
python3 -m venv venv
. venv/bin/activate
```
# Install fastapi, uvicorn, and gunicorn.
```pip install fastapi "uvicorn[standard]" gunicorn```
# Create the main.py file.
```nano main.py```
# Install pm2.
```sudo npm install -g pm2```
# Start pm2.
```pm2 start "gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app" --name hello_world```
# Verify that fastapi is running.
```curl localhost:8000```
# Configure nginx.
```
cd /etc/nginx/conf.d/
sudo nano default.conf
```
# Create a default.conf. Make sure to replace the IP address.
```
server {
  listen 80;

  server_name 123.456.789.10 example.com;

  location / {
    proxy_pass http://localhost:8000;
  }
}
```
# Restart nginx.
```sudo service nginx restart```
