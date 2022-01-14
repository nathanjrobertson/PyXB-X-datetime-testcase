# (pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$ docker compose up
# [+] Running 1/1
#  ⠿ Container pyxbx-datetime-bug-pyxbtest-1  Recreated                                                                                                                                                                                                                                    0.2s
# Attaching to pyxbx-datetime-bug-pyxbtest-1
# pyxbx-datetime-bug-pyxbtest-1  | (2022, 3, 11, 0, 0, 0, 0, None)
# pyxbx-datetime-bug-pyxbtest-1  | Traceback (most recent call last):
# pyxbx-datetime-bug-pyxbtest-1  |   File "test.py", line 20, in <module>
# pyxbx-datetime-bug-pyxbtest-1  |     period.twoDate = period.oneDate + relativedelta(days = -3)
# pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.8/site-packages/dateutil/relativedelta.py", line 405, in __radd__
# pyxbx-datetime-bug-pyxbtest-1  |     return self.__add__(other)
# pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.8/site-packages/dateutil/relativedelta.py", line 387, in __add__
# pyxbx-datetime-bug-pyxbtest-1  |     ret = (other.replace(**repl)
# pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.8/site-packages/pyxb/binding/datatypes.py", line 687, in __new__
# pyxbx-datetime-bug-pyxbtest-1  |     raise TypeError('function takes %d arguments plus optional tzinfo (%d given)' % (len(cls._ValidFields), len(args)))
# pyxbx-datetime-bug-pyxbtest-1  | TypeError: function takes 3 arguments plus optional tzinfo (8 given)
# pyxbx-datetime-bug-pyxbtest-1 exited with code 1
# (pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$


from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

from generated import protocol

period = protocol.someType()
period.lastUpdated = datetime.now()
period.oneDate = date.today() + relativedelta(months = + 2)
period.twoDate = period.oneDate + relativedelta(days = -3)
