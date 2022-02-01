heroku config:set DEBUG=$DEBUG_STAGING --app $HEROKU_APP_STAGING
heroku config:set ALLOWED_HOSTS=$ALLOWED_HOST_STAGING --app $HEROKU_APP_STAGING
heroku config:set THE_ONE_API_KEY=$THE_ONE_API_KEY --app $HEROKU_APP_STAGING
heroku config:set THE_ONE_API_URL=$THE_ONE_API_URL --app $HEROKU_APP_STAGING
heroku config:set SECRET_KEY=$SECRET_KEY_STAGING --app $HEROKU_APP_STAGING


heroku run python manage.py makemigrations --app $HEROKU_APP_STAGING
heroku run python manage.py migrate --app $HEROKU_APP_STAGING