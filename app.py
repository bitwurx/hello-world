import tornado.web
import tornado.ioloop


class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, World!')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'^/', HelloWorldHandler)
    ])
    app.listen(8080)
    torando.ioloop.IOLoop.current().start()
