#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:25:50 2020

@author: Yang
"""
from pyqrcode import *

dest=["0",
      "1",
      "2"]

for i in dest:
    myqr=QRCode(i)
    myqr.png("qrcodetest"+str(dest.index(i))+".png",scale=8)
    