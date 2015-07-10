__author__ = 'Roan Huang'

import sys


class _Const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            print("Can't change const.{key}".format(self))
            raise self.ConstError

        if not key.isupper():
            print("Const name \"{key}\" is not all uppercase".format(self))
            raise self.ConstCaseError

sys.modules[__name__] = _Const()
const = _Const


'''
Setting Globale Constant variable
'''
const.INTRO = """Welcome to OpenvSwitch console interface. Try type 'help' or '?' to list commands.\n"""
const.PROMPT = "ovs> "
const.VSCTL_SHOW = "ovs-vsctl: ovs-vswitchd management utility"
const.DEBUG_LEVEL = "DEBUG"
const.LOG_NAME = "OVS-CONSOLE"
