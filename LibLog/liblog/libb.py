import logging

from liba import ClassA

# create Module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the
# Application
module_logger.addHandler(logging.NullHandler())


class ClassB(ClassA):
    """No Logging config done here since all is done in the base ClassA"""

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')

def some_function():
    module_logger.info('received a call to "some_function"')
