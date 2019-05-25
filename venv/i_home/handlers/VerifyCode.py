from .BaseHandlers import BaseHandler
import logging
import constants
from i_home.utils.captcha.captcha import captcha

class ImageCodeHandler(BaseHandler):
    """"""
    def get(self):
        code_id = self.get_argument("codeid")
        pre_code_id = self.get_argument("pcodeid")
        if pre_code_id:
            try:
                self.redis.delete("")
            except Exception as e:
                logging.error(e)
            #name 图片验证码名称
            #text 图片验证码文本
            #image 图片验证码二进制数据
        name, text, image = captcha.generate_captcha()
        print(image)
        try:
            #设置前缀
            self.redis.setex("image_code_%s" % code_id, constants.IMAGE_CODE_EXPIRES_SECONDS, text)

        except Exception as e:
            logging.error(e)
            self.write("")
        self.set_header("Content-Type", "image/jpg")
        self.write(image)
