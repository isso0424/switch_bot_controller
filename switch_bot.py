import binascii
import gattlib
import bluetooth
from bluetooth.ble import DiscoveryService, GATTRequester
import argparse
import struct
import sys
import time


class Driver(object):
    handle = 0x16
    commands = {
        'press': '\x57\x01\x00',
        'on': '\x57\x01\x01',
        'off': '\x57\x01\x02',
    }

    def __init__(self, device, timeout_secs=None):
        self.device = device
        self.timeout_secs = timeout_secs if timeout_secs else 5
        self.req = None

    def connect(self):
        self.req = GATTRequester(self.device, False)
        self.req.connect(True, 'random')
        connect_start_time = time.time()
        while not self.req.is_connected():
            if time.time() - connect_start_time >= self.timeout_secs:
                raise RuntimeError('Connection to {} timed out after {} seconds'
                                   .format(self.device, self.timeout_secs))

    def run_command(self, command):
        return self.req.write_by_handle(self.handle, self.commands[command])


def main(timeout, addr, command):
    driver = Driver(device=addr, timeout_secs=timeout)
    driver.connect()
    print('Connected!')

    command_list = {
        'press': '\x57\x01\x00',
        'on': '\x57\x01\x01',
        'off': '\x57\x01\x02',
    }
    if command in command_list.keys():
        driver.run_command(command)
    else:
        ValueError("Command is press, on or off.")
    print("completed")


if __name__ == "__main__":
    main(10, "FC:5B:2F:10:D7:82", "on")
