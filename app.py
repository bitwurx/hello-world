import tornado.app
import tornado.ioloop


class HelloWorldHandler(tornado.app.RequestHandler):
    def get(self):
        self.write('Hello, World!')


if __name__ == '__main__':
    app = tornado.app.Application([v
        (r'^/', HelloWorldHandler)
    ])
    app.listen(80)
    torando.ioloop.IOLoop.current().start()
