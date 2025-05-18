#!/bin/bash

HOST=127.0.0.1
PORTS=(1111 2222 3333)

for port in "${PORTS[@]}"; do
    timeout 1 bash -c "</dev/tcp/$HOST/$port" &>/dev/null
    echo "Knocked on $port"
done
