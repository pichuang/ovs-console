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

def run_cmd(command):
    return call(command.split(' '))

class Shell(cmd.Cmd):

    intro = const.INTRO
    prompt = const.PROMPT

    def emptyline(self):
        pass

    # TODO: Show ovs-vsctl status

    def do_show(self, s):
        run_cmd("ovs-vsctl show")

    def do_list(self, s):
        run_cmd("ovs-vsctl list-br")

    def do_bridge(self, s):
        if s is not '':
            # exit 2 if BRIDGE does not exist
            if run_cmd("ovs-vsctl br-exists {bridge}".format(bridge=s)) == 2:
                logger.info("Create bridge {bridge}".format(bridge=s))
                run_cmd("ovs-vsctl add-br {bridge}".format(bridge=s))

            # TODO: delet bridge handle

            else:
                logger.debug("go to bridge cli")
        else:
            logger.info("Please type bridge name, like 'bridge ovs-br'")

    def do_version(self, s):
        # XXX: Need to aggregate information about ovs version
        run_cmd("ovs-vsctl --version")
        run_cmd("ovs-ofctl --version")


def main():
    """
    Main function of ovs-console
    """
    Shell().cmdloop()

if __name__ == "__main__":
    main()
