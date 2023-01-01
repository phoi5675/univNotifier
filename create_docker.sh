# Stop docker container.
docker stop webscrap
docker rm webscrap
# Recreate image.
docker build --rm -f dockerfiles/Dockerfile --tag scrapimg .
# Run dockeer container.
docker run -d --restart=always -v $(pwd):/webScrap --name webscrap scrapimg 
