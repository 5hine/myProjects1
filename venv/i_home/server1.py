import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import os
import sys

from tornado.options import define, options
from tornado.web import RequestHandler

import config
import urls
import torndb_for_python3
import redis

define("port", type=int, default=8004, help="run server on the given port")

class Application(tornado.web.Application):
    """"""
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        # self.db = torndb_for_python3.Connection(
        #     host=config.mysql_options("host"),
        #     database=config.mysql_options("database"),
        #     user=config.mysql_options("user"),
        #     password=config.mysql_options("password"),
        # )
        self.db = torndb_for_python3.Connection(**config.mysql_options)
        # self.redis = redis.StrictRedis(
        #     host="127.0.0.1",
        #     port=6379
        # )
        self.db = torndb_for_python3.Connection(**config.redis_options)


def main():
    options.logging = config.log_level
    options.log_file_prefix = config.log_file
    tornado.options.parse_command_line()    #执行 define 的字符串成 命令
    app = tornado.web.Application(
       urls.handlers,**config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    #http_server.listen(8000)
    #http_server.start(0)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()


