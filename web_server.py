from randomquotes import *
import cherrypy, datetime, os, os.path

if __name__ == '__main__':
    rootPath = os.path.abspath(os.getcwd())
    print("la racine du site est :\n\t{}\n\tcontient : {}".format(rootPath,os.listdir()))
    #On essaie de se connecter dès le lancement du serveur
    dbConnect()

    conf = {
        'global': {
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8080,
        }
    }

    cherrypy.quickstart(RandomQuotes(), '/', conf)
