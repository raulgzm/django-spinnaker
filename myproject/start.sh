#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn myproject.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --reload \
    --log-level debug
