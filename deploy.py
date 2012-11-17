from tornado import options
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from PythonForum import app

options.parse_command_line()

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(80)
IOLoop.instance().start()