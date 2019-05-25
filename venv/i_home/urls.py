import os

from i_home.handlers import Passport
from i_home.handlers import VerifyCode
from i_home.handlers import House
from tornado.web import StaticFileHandler

handlers = [
    #(r"/", Passport.IndexHandler),
    (r"/api/imagecode", VerifyCode.ImageCodeHandler),
    (r"/(.*)", StaticFileHandler, dict(path = os.path.join(os.path.dirname(
        __file__), "html"), default_filename = "index.html")),
    (r"/api/check_login", Passport.CheckLoginHandler), # 判断用户是否登录
    (r'^/api/house/index$', House.IndexHandler) # 首页
]