#!/bin/bash

exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --access-logfile=-


# #!/bin/bash

# set -e

# # Wait until MySQL is ready
# until mysqladmin ping -h"$MYSQL_HOST" -P"$MYSQL_PORT" --silent; do
#     echo 'Waiting for MySQL...'
#     sleep 1
# done

# # Apply migrations
# python manage.py migrate --noinput

# # Start Gunicorn
# exec gunicorn myproject.wsgi:application \
#     --bind 0.0.0.0:8000 \
#     --workers 4