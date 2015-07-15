#!/usr/bin/env python2

__author__ = 'Roan Huang'

import cmd
from utils.log import logger
from utils.util import *


class OVSShell(cmd.Cmd):
    intro = "Welcome to use OpenvSwitch Console"
    prompt = "ovs> "

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
        bridge_actions = ['list', 'add', 'delete', 'help', ]

        exist_bridge_list = list_br()
        line_list = line.split()
        logger.debug("Line: {line_list}, Text: {text}, List count: {count}".format(line_list=line_list, text=text,
                                                                                   count=len(line_list), end=''))

        # XXX: Maybe have some pretty work
        if line_list[1] == 'delete' and (len(line_list) == 2 or text not in exist_bridge_list):
            return auto_complete(text, exist_bridge_list)
        elif len(line_list) == 1 or text not in bridge_actions:
            return auto_complete(text, bridge_actions)

    def do_bridge(self, s):
        if s is not '':
            # XXX: need refactor
            # Split input string and convert from list to string
            command_list = s.split(' ')
            action_name = command_list[0]
            bridge_name = ""
            if len(command_list) >= 2:
                bridge_name = command_list[1]

            # Check bridge exists or not
            # retcode:
            # 0: exists
            # 1: no args
            # 2: not exists
            bridge_exists = False
            if run_cmd("ovs-vsctl br-exists {bridge}".format(bridge=bridge_name)).status_code == 0:
                bridge_exists = True

            logger.debug("DEBUG: command_list:{0} bridge_exists:{1} ".format(command_list, bridge_exists))

            # TODO: actions alias map, like 'delete == del'
            if action_name == "add":
                if bridge_exists is False and bridge_name is not '':
                    logger.info("Create bridge '{0}'".format(bridge_name))
                    run_cmd("ovs-vsctl add-br {0}".format(bridge_name))
                elif bridge_exists is True:
                    logger.info("Can't create bridge '{0}', because one bridge name same to its".format(
                        str(bridge_name)))
            elif action_name == "delete":
                # TODO: Enumerate all exists bridge, and do autocomplete
                if bridge_exists is True:
                    logger.info("Delete bridge '{0}'".format(bridge_name))
                    run_cmd("ovs-vsctl del-br {0}".format(bridge_name))
                elif bridge_exists is False:
                    logger.info("Can't delete not exists bridge '{0}'".format(bridge_name))
            elif action_name == "list":
                for result in list_br():
                    print(result)

        else:
            logger.info("Please type bridge name, like 'bridge help'")
            pass

    def do_health(self, s):

        ovsdb_server_status, ovs_vswitchd_status = False, False

        if s is not '':
            pass
        else:
            pass

    def do_version(self, s):
        # XXX: Need to aggregate information about ovs version
        run_cmd("ovs-vsctl --version")
        run_cmd("ovs-ofctl --version")


def main():
    """
    Main function of ovs-console
    """
    OVSShell().cmdloop()


if __name__ == "__main__":
    main()
