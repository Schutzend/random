from db_config import *

import cherrypy, datetime, os, os.path

class RandomQuotes(object):

    @cherrypy.expose()
    def index(self):
        #Get a random quote
        db,cursor = dbConnect()
        cursor.execute("SELECT author, quote FROM quotes ORDER BY RAND() LIMIT 1")
        res = cursor.fetchall()
        author = res[0]['author']
        quote = res[0]['quote']

        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Random Quotes</title>
            <style>

            </style>
        </head>
        <body>
            <div class="quoteText">
                “{quote}”
            <br>  ―
            <span class="authorOrTitle">
                {author}
            </span>
            </div>
        </body>
        </html>
        """
