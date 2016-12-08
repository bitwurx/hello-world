import tornado.web
import tornado.ioloop


class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, Jared!\n')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'^/', HelloWorldHandler)
    ])
    app.listen(8080)
    print('starting sever on :8080...')
    tornado.ioloop.IOLoop.current().start()
