#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography

# 画像にテキストを埋め込み
path = "Vol15_Q9.png"
secret_text = Steganography.decode(path)
print secret_text
