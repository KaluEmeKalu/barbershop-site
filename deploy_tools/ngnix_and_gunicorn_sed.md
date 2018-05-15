# Ngnix

## Create our Nginx virtual host

cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/superlists.bigballerbook.com/g" \
    | sudo tee /etc/nginx/sites-available/superlists.bigballerbook.com

## Activate File With symlink

sudo ln -s /etc/nginx/sites-available/superlists.bigballerbook.com \
    /etc/nginx/sites-enabled/superlists.bigballerbook.com

# Gunicorn

## Write Systemd Service

cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/superlists.bigballerbook.com/g" \
    | sudo tee /etc/systemd/system/gunicorn-superlists.bigballerbook.com.service

# Start Both Services

sudo systemctl daemon-reload
sudo systemctl reload nginx
sudo systemctl enable gunicorn-superlists.bigballerbook.com
sudo systemctl start gunicorn-superlists.bigballerbook.com

# Git Tag

git tag LIVE
export TAG=$(date +DEPLOYED-%F/%H%M)  # this generates a timestamp
echo $TAG # should show "DEPLOYED-" and then the timestamp
git tag $TAG
git push origin LIVE $TAG # pushes the tags up

# How to Deploy With Fab Command

fab deploy:host=kalu@superlists-staging.bigballerbook.com -u kalu