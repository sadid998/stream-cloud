#!/bin/sh
gunicorn main:main --workers 4 --threads 4 --bind 8000:$PORT --timeout 86400 --worker-class aiohttp.GunicornWebWorker & python -m bot
