import os
import pymysql, sqlite3

def dbConnect():
    #On lit les paramètres de connexion depuis les variables d'environnement
    db = pymysql.connect(host=os.environ.get('DB_HOST'), charset="utf8", user=os.environ.get('DB_USER'), passwd=os.environ.get('DB_PASSWORD'), db=os.environ.get('DB_NAME'))
    return (db,db.cursor(pymysql.cursors.DictCursor))

