import flask 
from flask import request, jsonify, Response
import requests
import time
import sys
import os
import logging
import datetime
from datetime import datetime
from lib.api_routes.example_routes import *
logging.basicConfig(filename='data/api.log', filemode="a+", format="%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s")

BOUND_PORT = 9501
BOUND_IP = "127.0.0.1"

class API_Server():
    def __init__(self):
        self.BOUND_PORT = BOUND_PORT
        self.BOUND_IP = BOUND_IP
        self.app = flask.Flask(__name__)
        self.app.config['DEBUG'] = False
        self.example_routes = Example_Routes()
        self.app.add_url_rule("/", "home", self.home)
        self.app.add_url_rule("/api/v1/resources/example/all", "report_all", self.example_routes.report_all, methods=['GET',])
        self.app.add_url_rule("/api/v1/resources/example/do_something", "do_something", self.example_routes.do_something, methods=['POST',])
        self.app.add_url_rule("/api/v1/resources/example/something_else", "something_else", self.example_routes.something_else, methods=['GET',])
    def home(self):
        return "<h1> API Server </h1>"
    def start_server(self):
        logging.warning("Starting API server")
        self.app.run(host=self.BOUND_IP, port=self.BOUND_PORT)
    def tearDown(self):
        func = request.environ.get("werkzeung.server.shutdown")
        func()


def main():
    api = API_Server()
    api.start_server()



if __name__ =="__main__":
    main()
