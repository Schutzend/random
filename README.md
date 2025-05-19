# Random Quotes

A simple app to get quotes from famous people.

## Requirements

You must have a mysql server with a database with read/write/create permissions.

## Installation

1. Get the code : download an archive or clone the repo at https://gitlab.iut-valence.fr/rambilm/random_quotes

2. cd to the working directory : `cd random_quotes`

3. Copy the file .env.dist to .env : `cp .env.dist .env`

4. Edit the .env file and set the proper values for the database access.

5. Run `./create_schema.sh` to create the necessary table.

6. Import the quotes from `quotes.csv` into the `quotes` table

## Running the development web server

Run the server : `./web_server.sh`

## Running using uWSGI

uWSGI is a Web Server Gateway Interface (WSGI) server implementation that is used to run Python web applications.

You can use the uwsgi_server.py file as an entrypoint for uWSGI

