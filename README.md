# Passaporto Checker

A simple tool to be notified for Italian passport request / renewal appointment availability

```bash
# Build the Docker image
docker build . -t passaporto-checker
# Run the container
docker run -d --name passaporto -v $(pwd):/usr/workspace:rw passaporto-checker
```