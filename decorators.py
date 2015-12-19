# -*- coding: utf-8 -*-

from time import sleep


def mc_sleep(ts):
    def tsleep(fn):
        def cfn(*args, **kws):
            print 'sleep ', ts, 'ms.'
            sleep(ts / 1000)
            print 'run farther'
            return fn(*args, **kws)

        return cfn

    return tsleep
