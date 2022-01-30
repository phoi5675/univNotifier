# Stop docker container.
docker stop webscrap
docker rm webscrap
# Recreate image.
docker build --rm -f dockerfiles/Dockerfile --tag scrapimg .
# Run dockeer container.
docker run -d -p 8000:8000 --restart=always -v "$((Get-Item -Path '.\' -Verbose).FullName)\webscrap:/webscrap" --name webscrap webscrap 