docker build --tag slideshowimage .

docker run -v /home/samuel/Pictures:/app/pictures -p 3000:3000 --name slideshowcontainer slideshowimage
