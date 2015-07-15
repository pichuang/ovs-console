__author__ = 'root'

import envoy

def run_cmd(command):
    return envoy.run(command)

def list_br():
    print(return_cmd("ovs-vsctl list-br"))
    return None

def auto_complete(text, list):
    if text:
        return [
                action for action in list if action.startswith(text)
                ]
    else:
        return list

# command = Cmd("ls").execute()
# print(command.getoutput())
