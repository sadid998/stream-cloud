import os

class Config:
    API_ID = int( os.getenv("api_id","1544329") )
    API_HASH = os.getenv("api_hash","e8c801b5516409dcf1549382cb350661")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001512858979") )
    CHANNEL_USERNAME = os.getenv("channel_username","Cinema_Great")
    TOKEN = os.getenv("token","1800448220:AAEUvwqFQVMKCnpL1EAkc1d1vunlOcSARRA")
    DOMAIN  = os.getenv("domain","https://cinemagreat.ml")
