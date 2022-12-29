import os
import sys
import time

with open("{}/data.json".format(os.getcwd()), "r") as f:
    data = f.read()


def report(module, action, exec_time):
    print("{} {} time: {:.2f}".format(module, action, exec_time))


def calc_load_json(data):
    import json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'load', exec_time)
    return load


def calc_dump_json(data):
    import json
    start_time = time.monotonic()
    load = json.dumps(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'dump', exec_time)
    return load


def calc_load_ujson(data):
    import ujson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'load', exec_time)
    return load


def calc_dump_ujson(data):
    import ujson as json
    start_time = time.monotonic()
    load = json.dumps(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'dump', exec_time)
    return load


def calc_load_nujson(data):
    import nujson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'load', exec_time)
    return load


def calc_dump_nujson(data):
    import nujson as json
    start_time = time.monotonic()
    load = json.dumps(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'dump', exec_time)
    return load


def calc_load_orjson(data):
    import orjson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'load', exec_time)
    return load


def calc_dump_orjson(data):
    import orjson as json
    start_time = time.monotonic()
    load = json.dumps(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'dump', exec_time)
    return load


def calc_load_simplejson(data):
    import simplejson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'load', exec_time)
    return load


def calc_dump_simplejson(data):
    import simplejson as json
    start_time = time.monotonic()
    load = json.dumps(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'dump', exec_time)
    return load


def calc_load_hjson(data):
    import hjson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'load', exec_time)
    return load


def calc_dump_hjson(data):
    import hjson as json
    start_time = time.monotonic()
    load = json.dumps(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'dump', exec_time)
    return load


def calc_load_rapidjson(data):
    import rapidjson as json
    start_time = time.monotonic()
    load = json.loads(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'load', exec_time)
    return load


def calc_dump_rapidjson(data):
    import rapidjson as json
    start_time = time.monotonic()
    load = json.dumps(data)
    exec_time = time.monotonic() - start_time
    report(json.__name__, 'dump', exec_time)
    return load


if sys.argv[1] == 'json':
    calc_dump_json(calc_load_json(data))
elif sys.argv[1] == 'ujson':
    calc_dump_ujson(calc_load_ujson(data))
elif sys.argv[1] == 'nujson':
    calc_dump_nujson(calc_load_nujson(data))
elif sys.argv[1] == 'hjson':
    calc_dump_hjson(calc_load_hjson(data))
elif sys.argv[1] == 'orjson':
    calc_dump_orjson(calc_load_orjson(data))
elif sys.argv[1] == 'python-rapidjson':
    calc_dump_rapidjson(calc_load_rapidjson(data))
elif sys.argv[1] == 'simplejson':
    calc_dump_simplejson(calc_load_simplejson(data))
