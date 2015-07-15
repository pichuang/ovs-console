__author__ = 'root'

import envoy

def run_cmd(command):
    return envoy.run(command)

def list_br():
    output = run_cmd("ovs-vsctl list-br").std_out
    result = output.split('\n')
    del result[-1]  # Delete useless element in list
    return result

def auto_complete(text, list):
    if text:
        return [
                action for action in list if action.startswith(text)
                ]
    else:
        return list

