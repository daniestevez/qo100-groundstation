#!/usr/bin/env python3

import datetime
import time

TIMEOUT = 15 * 60
GPIO = '/sys/class/gpio/gpio116/value'

on_since = None
while True:
    with open(GPIO) as gpio:
        value = int(gpio.read())
    if value == 0:
        on_since = None
    elif on_since is None:
        on_since = datetime.datetime.utcnow()
    elif (datetime.datetime.utcnow() - on_since).total_seconds() > TIMEOUT:
        print('Watchdog timeout')
        with open(GPIO, 'w') as gpio:
            gpio.write('0\n')
        on_since = None
    time.sleep(1)

