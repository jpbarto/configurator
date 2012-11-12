"""
########################################
# Command Line Option Block:
# { 
#     'param_long' : <LONG COMMAND LINE OPTION NAME>,
#     'param_short': <SHORT COMMAND LINE OPTION NAME>,
#     'type'       : <ONE OF str (string), bool (boolean), int (integer), float (float)>,
#     'default'    : <DEFAULT CONFIGURATION VALUE>,
#     'help'       : <TEXTUAL DESCRIPTION OF CONFIGURATION PARAMETER>
# }
#
# Configuration File Option Block:
# {
#     'name'       : <CONFIGURATION FILE PARAMETER NAME>,
#     'section'    : <NAME OF CONFIGURATION FILE SUBSECTION>,
#     'type'       : <ONE OF str (string), bool (boolean), int (integer), float (float)>,
#     'default'    : <DEFAULT CONFIGURATION VALUE>,
#     'help'       : <TEXTUAL DESCRIPTION OF CONFIGURATION PARAMETER>
# }
#
# Combined Command Line / Configuration File Block:
# {
#     'name'       : <CONFIGURATION FILE PARAMETER NAME>,
#     'section'    : <NAME OF CONFIGURATION FILE SUBSECTION>,
#     'param_long' : <LONG COMMAND LINE OPTION NAME>,
#     'param_short': <SHORT COMMAND LINE OPTION NAME>,
#     'type'       : <ONE OF str (string), bool (boolean), int (integer), float (float)>,
#     'default'    : <DEFAULT CONFIGURATION VALUE>,
#     'help'       : <TEXTUAL DESCRIPTION OF CONFIGURATION PARAMETER>
# }
#
# Example:
# {
#     'name'       : 'log_level'
#     'section'    : 'logging'
#     'param_long' : 'loglevel'
#     'param_short': 'v'
#     'type'       : str
#     'default'    : 'warning'
#     'help'       : 'Set the output level of log messages'
# }
########################################
"""

import os
import re
import optparse
import cfgparse

_optp = optparse.OptionParser ();
_confp = cfgparse.ConfigParser ()
_confp.add_optparse_help_option (_optp)

def load_configuration (param_config):
    global _optp, _confp

    for param in param_config:
        if 'param_long' in param or 'param_short' in param:
            add_option_param (param)
        if 'name' in param:
            add_config_param (param)

    return _optp.parse_args ()[0]

def read_configuration (filename):
    global _optp, _confp
    err = []
    if os.access (filename, os.R_OK):
        _confp.add_file (filename)
    else:
        err.append ("Configuration file {} does not exist or is not readable.".format (filename))

    conf, perrs = _confp.parse (_optp)
    err.extend (perrs)
    return conf, err

def add_option_param (param):
    global _optp
    assert 'param_short' in param or 'param_long' in param, "Setting passed without parameter names specified"

    cmdFields = []
    if 'param_short' in param:
        cmdFields.append (re.sub (r'^([A-Za-z0-9])', r'-\1', param['param_short']))
    if 'param_long' in param:
        cmdFields.append (re.sub (r'^([A-Za-z0-9])', r'--\1', param['param_long']))

    kargs = {}
    if 'name' in param:
        kargs['dest'] = param['name']
    if 'default' in param:
        kargs['default'] = param['default']
    if 'help' in param:
        kargs['help'] = param['help']
    if 'type' in param:
        if param['type'] is bool:
            kargs['action'] = 'store_false'
            if 'default' in param and param['default'] is True:
                kargs['action'] = 'store_true'
        elif param['type'] is int:
            kargs['type'] = 'int'
        elif param['type'] is float:
            kargs['type'] = 'float'
        else:
            kargs['type'] = 'string'

    _optp.add_option (*cmdFields, **kargs)

def add_config_param (param):
    global _confp
    args = []
    kargs = {}
    assert 'name' in param, "Parameter passed without a name field"
    
    args.append (param['name'])
    if 'help' in param:
        kargs['help'] = param['help']

    def check_bool (val):
        return bool(val), None

    if 'type' in param:
        if param['type'] == bool:
            kargs['check'] = check_bool
        elif param['type'] == int:
            kargs['type'] = 'int'
        elif param['type'] == float:
            kargs['type'] = 'float'
        else:
            kargs['type'] = 'string'
    if 'default' in param:
        kargs['default'] = param['default']
    if 'section' in param:
        kargs['keys'] = param['section']

    _confp.add_option (*args, **kargs)
