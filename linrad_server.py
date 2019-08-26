#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# 
# Copyright 2019 Daniel Estevez <daniel@destevez.net>
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 


import struct
import socket
import threading

def server():
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn, ))
            t.start()

def handle_client(conn):
        try:
                while True:
                        data = conn.recv(1024)
                        if not data: break
                        if len(data) == 0: continue
                        if data[0] == '\xb8':
                                response = struct.pack('<8i', samp_rate, ad_channels,\
                                                        rf_channels, input_mode, bufsize, 0, 0, 0)
                                conn.send(response)
                        elif data[0] == '\xb5' or data[0] == '\xb6':
                                conn.send('\x00')
        finally:
            conn.close()

listen_ip = '0.0.0.0'
samp_rate = 300e3
ad_channels = 2
rf_channels = 1
bufsize = 4096
# input mode = 1 -> DWORD_INPUT
# input mode = 4 -> IQ_DATA
input_mode = 4

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listen_ip, 49812))
s.listen(1)
        
t = threading.Thread(target=server)
t.start()
