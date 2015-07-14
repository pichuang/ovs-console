__author__ = 'root'

from subprocess import call
import subprocess

def run_cmd(command):
    return call(command.split(' '))

def return_cmd(command):
    return subprocess.check_output(command)

def list_br():
    print(return_cmd("ovs-vsctl list-br"))
    return None

class Cmd(object):
    def __init__(self, command=""):
        self.cmd = command
        self.process = None

    def execute(self):
        self.process = subprocess.Popen(self.cmd.split(), stdout=subprocess.PIPE)
        return self.process

    def getoutput(self):
        return self.process.communicate()[0]

    def getretcode(self):
        pass

# print("="*5)
# command = Cmd("ls").execute()
# print(command.getoutput())
