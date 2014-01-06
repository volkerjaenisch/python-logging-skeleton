import logging

# create file handler which logs even debug messages
fh = logging.FileHandler('main.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# These logging config determines the appearence of the application log
# in the namespace "applog.*"
# create logger "applog"
applog = logging.getLogger('applog')
applog.setLevel(logging.DEBUG)

# add the handlers to the logger
applog.addHandler(fh)
applog.addHandler(ch)

# These logging config determines the appearence of the application log
# in the namespace "liblog.*"

# configure logger "liblog"
liblog = logging.getLogger('liblog')
liblog.setLevel(logging.DEBUG)

# add the handlers to the logger
liblog.addHandler(fh)
liblog.addHandler(ch)
