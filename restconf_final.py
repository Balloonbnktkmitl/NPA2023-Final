import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.189
api_url = "https://10.0.15.233/restconf" # Add

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
# <!!!REPLACEME with Accept and Content-Type information headers!!!>
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
} # Add
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070021",
            "description": "created loopback by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.30.21.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    } # Add

    resp = requests.put(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070021", # Add
        data=json.dumps(yangConfig), # Add
        auth=basicauth, 
        headers=headers, # Add 
        verify=False
        )

    if(resp.status_code == 204):
        return "Cannot create: Interface loopback 66070021" # Add
    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface Loopback65070021 created."
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def delete():
    resp = requests.delete(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070021", # Add
        auth=basicauth, 
        headers=headers, # Add
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface Loopback65070021 deleted."
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot delete: Interface loopback 66070021" # Add


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070021",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
        } # Add
    }

    resp = requests.patch(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070021", # Add
        data=json.dumps(yangConfig), # Add
        auth=basicauth, 
        headers=headers, # Add
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 66070123 is enabled successfully" # Add
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot enable: Interface loopback 66070021" # Add
        


def disable():
    yangConfig = yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070021",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False,
        } # Add
    }

    resp = requests.patch(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070021", # Add
        data=json.dumps(yangConfig), # Add
        auth=basicauth, 
        headers=headers, # Add
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070104 is disabled" # Add
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot shutdown: Interface loopback 65070104" # Add


def status():
    api_url_status = "<!!!REPLACEME with URL of RESTCONF Operational API!!!>"

    resp = requests.<!!!REPLACEME with the proper HTTP Method!!!>(
        <!!!REPLACEME with URL!!!>, 
        auth=basicauth, 
        headers=<!!!REPLACEME with HTTP Header!!!>, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = <!!!REPLACEME!!!>
        oper_status = <!!!REPLACEME!!!>
        if admin_status == 'up' and oper_status == 'up':
            return "<!!!REPLACEME with proper message!!!>"
        elif admin_status == 'down' and oper_status == 'down':
            return "<!!!REPLACEME with proper message!!!>"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "<!!!REPLACEME with proper message!!!>"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
