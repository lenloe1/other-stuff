
import imp
import os

_PKG_PATH = os.path.dirname(os.path.realpath(__file__))
__all__ = ['RM_Factory']

_RM_PART_FAMILY_MAP = {
    'DUMBO':   'host_py_rm_studio_internal_efr32xg1xfull',
    'JUMBO':   'host_py_rm_studio_internal_efr32xg12xfull',
    'NERIO':   'host_py_rm_studio_internal_efr32xg13xfull',
    'NIXI':    'host_py_rm_studio_internal_efr32xg14xfull',
    'PANTHER': 'host_py_rm_studio_internal_efr32x21x000f1024xm32',
    'LYNX':    'host_py_rm_studio_internal_efr32xg22x000f512im32',
}


def RM_Factory(part_family_name, part_rev_name=None):

    try:
        mod_name = _RM_PART_FAMILY_MAP[part_family_name]
    except KeyError:
        raise KeyError("Invalid family name '{}'".format(part_family_name))

    die_path = os.path.join(_PKG_PATH, mod_name)
    die_pkg = imp.load_module(mod_name, None, die_path, ('', '', 5))
    factory_func = getattr(die_pkg.factory, 'RM_Factory')
    return factory_func(part_rev_name)


if __name__ == '__main__':
    from host_py_rm_studio_internal import RM_Factory
    # latest
    for die_name in ['DUMBO', 'JUMBO', 'NERIO', 'NIXI', 'PANTHER', 'LYNX']:
        factory_latest = RM_Factory(die_name)
        rm = factory_latest()
    # explict
    for rev in ['A2', 'A3']:
        factory_rev = RM_Factory('DUMBO', rev)
        rm = factory_rev()
        print(rm)
    for rev in ['A0', 'A1', 'A2']:
        factory_rev = RM_Factory('JUMBO', rev)
        rm = factory_rev()
        print(rm)
    for rev in ['A0', 'A1', 'A2']:
        factory_rev = RM_Factory('NERIO', rev)
        rm = factory_rev()
        print(rm)
    for rev in ['A0', 'A1']:
        factory_rev = RM_Factory('NIXI', rev)
        rm = factory_rev()
        print(rm)
    for rev in ['A0', 'A1']:
        factory_rev = RM_Factory('PANTHER', rev)
        rm = factory_rev()
        print(rm)
    for rev in ['A0']:
        factory_rev = RM_Factory('LYNX', rev)
        rm = factory_rev()
        print(rm)
