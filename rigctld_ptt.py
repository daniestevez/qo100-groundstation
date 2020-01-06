#!/usr/bin/env python3

import socket

LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 4532
BUFFER_SIZE = 1024
GPIO = '/sys/class/gpio/gpio116/value'

STATE = b"""0
1
2
150000.000000 1500000000.000000 0x1ff -1 -1 0x10000003 0x3
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0x1ff 1
0x1ff 0
0 0
0x1e 2400
0x2 500
0x1 8000
0x1 2400
0x20 15000
0x20 8000
0x40 230000
0 0
9990
9990
10000
0
10 
10 20 30 
0xffffffff
0xffffffff
0xf7ffffff
0x83ffffff
0xffffffff
0xffffffbf
"""

class PTT:
    def __init__(self):
        self.gpio = open(GPIO, 'w')
        self.set(0)
    def set(self, state):
        self.state = 1 if state else 0
        self.gpio.seek(0)
        self.gpio.write('1\n' if state else '0\n')
        self.gpio.flush()
        print('ptt set to', self.state)
        
    def get(self):
        return self.state

def main():
    ptt = PTT()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((LISTEN_IP, LISTEN_PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print('Connection from', addr)
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            if data == b'\\dump_state\n':
                conn.send(STATE)
            elif data == b'v\n':
                conn.send(b'VFOA\n')
            elif data == b't\n':
                conn.send(bytes(str(ptt.get()) + '\n', encoding = 'ascii'))
            elif data == b'f\n':
                conn.send(b'145000000\n')
            elif data == b'm\n':
                conn.send(b'USB\n15000\n')
            elif data.startswith(b'T '):
                ptt.set(int(data.split()[1]))
                conn.send(b'RPRT 0\n')
            else:
                conn.send(b'\n')
        conn.close()
    

if __name__ == '__main__':
    main()
