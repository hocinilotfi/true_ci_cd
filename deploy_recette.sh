# run the image if not already running
docker rm -f api_for_cicd_rec_service || true
docker run -d -p 8002:8001 --name api_for_cicd_rec_service lotfihocini/api_for_cicd:latest