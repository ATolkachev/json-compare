import os
import sys
import time

with open("{}/imdb.json".format(os.getcwd()), "r") as f:
    data = f.read()


def calc_load_json(data):
    import json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    print("json load time: {}".format(exec_time))
    return load


def calc_dump_json(data):
    import json
    start_time = time.monotonic()
    load = json.dumps(data)
    exec_time = time.monotonic() - start_time
    print("json dump time: {}".format(exec_time))
    return load


def calc_load_ujson(data):
    import ujson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    print("ujson load time: {}".format(exec_time))
    return load


def calc_load_nujson(data):
    import nujson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    print("nujson load time: {}".format(exec_time))
    return load


def calc_load_orjson(data):
    import orjson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    print("orjson load time: {}".format(exec_time))
    return load


def calc_load_simplejson(data):
    import simplejson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    print("simplejson load time: {}".format(exec_time))
    return load


def calc_load_hjson(data):
    import hjson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    print("hjson load time: {}".format(exec_time))
    return load


def calc_load_rapidjson(data):
    import rapidjson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    print("rapidjson load time: {}".format(exec_time))
    return load


if sys.argv[1] == 'json':
    calc_dump_json(calc_load_json(data))
elif sys.argv[1] == 'ujson':
    calc_load_ujson(data)
elif sys.argv[1] == 'nujson':
    calc_load_nujson(data)
elif sys.argv[1] == 'hjson':
    calc_load_hjson(data)
elif sys.argv[1] == 'orjson':
    calc_load_orjson(data)
elif sys.argv[1] == 'python-rapidjson':
    calc_load_rapidjson(data)
elif sys.argv[1] == 'simplejson':
    calc_load_simplejson(data)
