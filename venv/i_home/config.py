import os

#Application配置参数
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "templates": os.path.join(os.path.dirname(__file__), "template"),
    "debug":True,
    "cookie_secret":"824a3b34f9e44b159583e26816c46e4f", #一般是用着base64(uuid4())
    "xsrf_cookies":True
}

#mysql
mysql_options = dict(
    host = "127.0.0.1",
    database = "ihome",
    user = "root",
    password = "mysql"
)

#reids
redis_options = dict(
    host="127.0.0.1",
    port=6379
)

log_file = os.path.join(os.path.dirname(__file__), "logs/log")
log_level = "debug"