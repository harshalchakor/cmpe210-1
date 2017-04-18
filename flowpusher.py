#using to learn how to push the flow rule
import httplib
import json
  
class StaticFlowPusher(object):
  
    def __init__(self, server):
        self.server = server
  
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
  
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
  
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
  
    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret
  
pusher = StaticFlowPusher('10.0.2.15')
  
flow1 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow_mod_1",
    "cookie":"0x0F",
    "priority":"0",
    "in_port":"1",
    "active":"true",
    "actions":"output=flood"
    }
  
flow2 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_2",
    "cookie":"0x0F",
    "priority":"110",
    "in_port":"2",
    "active":"true",
    "actions":"output=flood"}
  
pusher.set(flow1)
pusher.set(flow2)
