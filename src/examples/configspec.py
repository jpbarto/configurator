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

CONFIG_SPEC = (
    {
        "name": "debug",
        "param_long": "debug",
        "param_short": "D",
        "type": bool,
        "default": 0,
        "help": "Run with debugging information enabled, producing a lot of output"
    },
    {
        "name": "conffile",
        "param_long": "config",
        "param_short": "c",
        "type": str,
        "default": "xmimd.conf",
        "help": "Path to XMIM Configuration File"
    },
    {
        "name": "log_filename",
        "default": "xmimd.log",
        "type": str,
        "help": "Path to XMIM Log File",
        "param_long": "logfile",
        "param_short": "l",
        "section": "xmimd.logging"
    },
    {
        "name": "log_level",
        "default": "warning",
        "type": str,
        "help": "Level of criticality required to log a message",
        "section": "xmimd.logging"
    }
)
