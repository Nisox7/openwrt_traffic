from dotenv import load_dotenv
import os

load_dotenv()
#App

update_interval = os.getenv("UPDATE_INTERVAL")

#DB

database_host = os.getenv("DATABASE_HOST")
database_name = os.getenv("DATABASE_NAME")
database_table = os.getenv("DATABASE_TABLE")
database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")

#OpenWRT

openwrt_ip = os.getenv("OPENWRT_IP")
openwrt_user = os.getenv("OPENWRT_USER")
openwrt_password = os.getenv("OPENWRT_PASSWORD")
openwrt_interface = os.getenv("OPENWRT_INTERFACE")
