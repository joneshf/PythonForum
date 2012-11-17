from tornado import options
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from PythonForum import app

options.parse_command_line()
options.options['log_file_prefix'].set('.python-forum.log')

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8001)
http_server.listen(8002)
http_server.listen(8003)
http_server.listen(8004)
IOLoop.instance().start()