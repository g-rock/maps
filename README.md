### Docker container running jupyter with dependencies installed:
```
docker run --rm -it -p 8888:8888 -v "$PWD":/maps gboeing/osmnx:latest
```