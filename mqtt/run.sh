#!/bin/bash
#docker stop mqtt
#docker rm mqtt

`which docker` run \
    --name mqtt \
    --net host \
    --rm \
    -v /etc/localtime:/etc/localtime:ro \
    -v /home/$1/mqtt/config:/mosquitto/config:ro \
    -v /home/$1/mqtt/data:/mqtt/data:rw \
    eclipse-mosquitto
