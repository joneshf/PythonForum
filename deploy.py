from twisted.internet import reactor
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site

from PythonForum import app

resource = WSGIResource(reactor, reactor.getThreadPool(), app)
site = Site(resource)

reactor.listenTCP(8080, site)
reactor.run()