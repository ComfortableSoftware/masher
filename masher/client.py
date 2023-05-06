

import os

_fifo_ = "/tmp/pipe1Liam"
with open(_fifo_, "tw") as _FDOut_:
  _strToWrite_ = f"""Having some fun now with {_fifo_}"""
  _FDOut_.write(_strToWrite_)


#
