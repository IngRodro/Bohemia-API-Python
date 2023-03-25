import os

mongo_uri :str = os.environ.get('MONGO_URI')

cloud_config: dict = {
    "cloud_name" : os.environ.get('APP_CLOUD_NAME'),
    "api_key" : os.environ.get('APP_API_KEY'),
    "api_secret" : os.environ.get('APP_API_SECRET')
}
