#!/bin/bash

docker build -t art_image . --rm
MSYS_NO_PATHCONV=1 docker run -it --name art -v "$(pwd)/data:/home/root/data" --rm art_image $1