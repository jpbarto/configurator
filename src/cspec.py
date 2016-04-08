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
