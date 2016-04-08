import configurator as confr
from cspec import CONFIG_SPEC

confr.load_configuration (CONFIG_SPEC)
c = confr.read_configuration ('conf.file')
