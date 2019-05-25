from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    """handler基类"""
    @property
    def db(self):
        return self.application.db

    @property
    def redis(self):
        return self.application.reids

    def prepare(self):
        pass

    def write_error(self, status_code: int, **kwargs: any):
        pass

    def set_default_headers(self):
        pass

    def _initialize(self):
        pass

    def on_finish(self):
        pass
