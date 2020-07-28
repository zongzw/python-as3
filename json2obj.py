import json
from collections import namedtuple

def dictDecoder(mydict):
    return namedtuple('X', mydict.keys())(*mydict.values())

with open('./testdata/loadbalancer-full-create-request.json') as fr:
    lb = json.load(fr, object_hook=dictDecoder)
    print(
        lb.loadbalancer.project_id, 
        lb.loadbalancer.listeners[0].default_pool.members,
        lb.loadbalancer.listeners[0].default_pool.name,
        lb.loadbalancer.listeners[0].default_pool.healthmonitor.type,
    )

    m = lb.loadbalancer.listeners[0].default_pool.members

    print(m[0].address)