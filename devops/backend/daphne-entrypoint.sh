#!/bin/sh


cd backend  # <-- Katalogni o'zgartirish

echo 'Running daphne server...'
daphne -b 0.0.0.0 -p 8001 config.asgi:application
