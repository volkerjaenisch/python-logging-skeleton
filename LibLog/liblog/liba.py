import logging

# create Module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the
# Application
module_logger.addHandler(logging.NullHandler())

class ClassA:
    def __init__(self):
        # create Class logger
        # self.__module__ ensures that the right module path is set to the
        # logger suffix.
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)
        # Add a NullHandler for the case if no logging is configured by the
        # Application
        self.logger.addHandler(logging.NullHandler())
        # Do some logging at creation time
        self.logger.info('creating an instance of %s', self.__class__.__name__)

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')

def some_function():
    module_logger.info('received a call to "some_function"')
