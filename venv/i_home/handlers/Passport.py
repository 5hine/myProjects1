from i_home.handlers.BaseHandlers import BaseHandler
import logging


class IndexHandler(BaseHandler):
    def get(self):
        #self.application.db   太麻烦，在base 中 定义 db函数
        #self.application.reids
        logging.debug("debug msg")
        logging.info("info msg")
        logging.warning("warning msg")
        logging.error("error msg")
        print("pritn msg")
        self.write("hello !")


class CheckLoginHandler(BaseHandler):
    def get(self):
        pass

