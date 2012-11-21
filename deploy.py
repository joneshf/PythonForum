from twisted.internet import reactor
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.python import log
from twisted.python.logfile import DailyLogFile

from sys import stdout

from PythonForum import app

log.startLogging(stdout)
log.startLogging(DailyLogFile("python-forum.log", "."))

resource = WSGIResource(reactor, reactor.getThreadPool(), app)
site = Site(resource)

reactor.listenTCP(8080, site)
reactor.run()