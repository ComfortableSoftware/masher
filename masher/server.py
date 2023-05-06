#!/usr/bin/env /usr/bin/python


import os
import errno


_fifo_ = "/tmp/pipe1Liam"

try:
  os.mkfifo(_fifo_)
except OSError as e:
  if (
      (e.errno != errno.EEXIST)
  ):
    raise

with open(_fifo_, "tr") as _FDIn_:
  while True:
    _data_ = _FDIn_.read()

    if (
        (len(_data_) != 0)
    ):
      print(f"""Got a whoopty {_data_}""")


#
