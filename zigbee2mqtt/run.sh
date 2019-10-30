#!/bin/bash
#docker stop zigbee2mqtt
#docker rm zigbee2mqtt

`which docker` run \
    --device /dev/ttyACM0:/dev/ttyACM0 \
    --name zigbee2mqtt \
    --net host \
    --rm \
    -v /etc/localtime:/etc/localtime:ro \
    -v /home/$1/zigbee2mqtt/data:/app/data:rw \
    koenkk/zigbee2mqtt:latest
