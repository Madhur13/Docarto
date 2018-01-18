# Important for Heroku
BASE_DIR = dirname(dirname(abspath(__file__)))

STATIC_ROOT = 'static' # Important for Heroku
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    path.join(BASE_DIR, 'static'),  # Important for Heroku
)
