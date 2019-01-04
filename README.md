docker build . -t test-passaporto
docker run -d --name passaporto -v $(pwd):/usr/workspace:rw test-passaporto