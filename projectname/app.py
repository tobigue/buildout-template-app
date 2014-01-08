import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.options import options


class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        self.write("Hello, world")


def start_app():
    tornado.options.parse_command_line()
    tornado_settings = {
        "xheaders": True,
        "debug": options.debug,
    }
    app = tornado.web.Application(handlers=[
        (r'/', MainHandler)
    ], **tornado_settings)
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port, address=options.host)
    tornado.ioloop.IOLoop.instance().start()
