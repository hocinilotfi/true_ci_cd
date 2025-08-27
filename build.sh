# build the image the docker api_for_ci image to docker hub
docker build -t api_for_cicd .
docker tag api_for_cicd lotfihocini/api_for_cicd:latest
docker push lotfihocini/api_for_cicd:latest

