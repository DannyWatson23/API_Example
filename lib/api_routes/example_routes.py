from flask import Response, jsonify, request
import logging
import json
from random import randint
from random import seed
from datetime import datetime
logger = logging.getLogger()

class Example_Routes():
    '''
    do_something -> curl --request POST 'localhost:9501/api/v1/resources/example/do_something'  --header 'Content-Type: application/json'  --data-raw '{"a": 4, "b": 10}'
    report_all -> curl 'localhost:9501/api/v1/resources/example/all'
    something_else -> curl 'localhost:9501/api/v1/resources/example/something_else'
    '''
    def __init__(self):
        logging.info("Setting up Example_Routes()")
        pass
    def do_something(self):
        '''
            This function will accept two variables 'a' and 'b', it will then add them together and return

            a -> int
            b -> int

        '''
        logging.info("Inside do_something()")
        do_something_dict = {}
        if not request.json:
            return Response("JSON format required!", 400)
        if 'a' not in request.json or 'b' not in request.json:
            return Response("Variables a and b are required!", 400)
        else:
            do_something_dict['a'] = request.json['a']
            do_something_dict['b'] = request.json['b']
            do_something_dict['c'] = int(request.json['a']) + int(request.json['b'])
            logging.info(str(do_something_dict))
            return jsonify(do_something_dict)

    def report_all(self):
        '''
            Simply generates a random float and returns
        '''
        logging.warning("Inside report_all")
        a = randint(0, 2000)
        return jsonify(a)

    def something_else(self):
        '''
            Returns the current date
        '''
        logging.debug("Inside something_else")
        now = datetime.now()
        _ = {}
        _["current_date"] = now
        return jsonify(_)