__author__ = 'root'

from subprocess import call

# TODO: Need move to util.py
def run_cmd(command):
    return call(command.split(' '))
