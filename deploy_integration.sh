# run the image if not already running
# remove existing container if it exists
docker rm -f api_for_cicd_int_service || true
docker run -d -p 8001:8001 --name api_for_cicd_int_service lotfihocini/api_for_cicd:latest