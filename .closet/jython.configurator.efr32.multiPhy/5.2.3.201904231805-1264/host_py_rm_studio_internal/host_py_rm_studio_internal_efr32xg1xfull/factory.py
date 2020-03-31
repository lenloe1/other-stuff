
import imp
import os

_DIE_NAME = 'EFR32XG1XFULL'
_SUPPORTED = ['A2','A3']

_PKG_PATH = os.path.dirname(os.path.realpath(__file__))


def RM_Factory(part_rev_name):

    if part_rev_name is None:
        part_rev_name = _SUPPORTED[-1]
    elif part_rev_name not in _SUPPORTED:
        raise ValueError("Invalid part revision {}".format(part_rev_name))

    mod_name = os.path.basename(_PKG_PATH) + '.rev' + part_rev_name
    rev_path = os.path.join(_PKG_PATH, 'rev' + part_rev_name)
    rev_pkg = imp.load_module(mod_name, None, rev_path, ('', '', 5))

    return getattr(rev_pkg, 'RM_Device_' + _DIE_NAME + '_Rev' + part_rev_name)
