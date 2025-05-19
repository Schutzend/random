from randomquotes import *
import cherrypy, datetime, os, os.path
from dotenv import load_dotenv

load_dotenv()
cherrypy.config.update({'engine.autoreload.on': False})
cherrypy.server.unsubscribe()
cherrypy.engine.start()

wsgiapp = cherrypy.tree.mount(RandomQuotes())
