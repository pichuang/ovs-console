__author__ = 'Roan Huang'

import cmd
from subprocess import call
from util import const

'''
Log handler
'''
import logging

LEVEL = const.DEBUG_LEVEL
logger = logging.getLogger(const.LOG_NAME)
logger.setLevel(LEVEL)
console = logging.StreamHandler()
console.setLevel(LEVEL)
logger.addHandler(console)

# TODO: Need move to util.py
def run_cmd(command):
    return call(command.split(' '))


bridge_actions = [
    'list',
    'add',
    'delete',
    'help',
]

class OVS_Shell(cmd.Cmd):

    intro = const.INTRO
    prompt = const.PROMPT

    def emptyline(self):
        pass

    # TODO: Find and check binary path
    # TODO: Find and check service daemon work well

    def do_show(self, s):
        run_cmd("ovs-vsctl show")

    def do_list(self, s):
        run_cmd("ovs-vsctl list-br")


    """
    Bridge handle
    - complete_bridge
    - do_bridge
    """
    def complete_bridge(self, text, line, start_index, end_index):
        # XXX: Maybe have some pretty work
        if text:
            return [
                action for action in bridge_actions
                if action.startswith(text)
            ]
        else:
            return bridge_actions

    def do_bridge(self, s):
        if s is not '':
            # Split input string and convert from list to string
            action_name, *bridge_name = s.split(' ')
            action_name = ''.join(action_name)
            if bridge_name is not '':
                bridge_name = ''.join(bridge_name)

            # Check bridge exists or not
            bridge_exists = True
            if run_cmd("ovs-vsctl br-exists {bridge}".format(bridge=bridge_name)) == 2:
                bridge_exists = False

            logger.debug("DEBUG: action_name:{0} bridge_name:{1} bridge_exists:{2}".format(action_name, bridge_name, bridge_exists))

            # TODO: actions alias map, like 'delete == del'
            if action_name == "add":
                if bridge_exists is False:
                    logger.info("Create bridge '{bridge}'".format(bridge=bridge_name))
                    run_cmd("ovs-vsctl add-br {bridge}".format(bridge=bridge_name))
                elif bridge_exists is True:
                    logger.info("Can't create bridge '{bridge}', because one bridge name same to its".format(bridge=str(bridge_name)))
            elif action_name == "delete":
                # TODO: Enumerate all exists bridge, and do autocomplete
                if bridge_exists is True:
                    logger.info("Delete bridge '{bridge}'".format(bridge=bridge_name))
                    run_cmd("ovs-vsctl del-br {bridge}".format(bridge=bridge_name))
                elif bridge_exists is False:
                    logger.info("Can't delete not exists bridge '{bridge}'".format(bridge=bridge_name))
            if action_name == "list":
                run_cmd("ovs-vsctl list-br")

        else:
            logger.info("Please type bridge name, like 'bridge help'")
            pass

    def do_version(self, s):
        # XXX: Need to aggregate information about ovs version
        run_cmd("ovs-vsctl --version")
        run_cmd("ovs-ofctl --version")


def main():
    """
    Main function of ovs-console
    """
    OVS_Shell().cmdloop()


if __name__ == "__main__":
    main()
