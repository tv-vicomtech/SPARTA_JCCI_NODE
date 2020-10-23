#!/bin/bash
cd /home/ && python3.7 flaskserver.py &
./docker-entrypoint.sh
