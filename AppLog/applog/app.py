from applog.log import applog

from liblog import liba
from liblog import libb


applog.info('creating an instance of liba.ClassA')
a = liba.ClassA()
applog.info('created an instance of liba.ClassA')
applog.info('calling liba.ClassA.do_something')
a.do_something()
applog.info('finished liba.ClassA.do_something')
applog.info('calling liba.some_function()')
liba.some_function()
applog.info('done with liba.some_function()')

applog.info('creating an instance of libb.ClassB')
b = libb.ClassB()
applog.info('created an instance of libb.ClassB')
applog.info('calling libb.ClassB.do_something')
b.do_something()
applog.info('finished libb.ClassB.do_something')
applog.info('calling libb.some_function()')
libb.some_function()
applog.info('done with libb.some_function()')
