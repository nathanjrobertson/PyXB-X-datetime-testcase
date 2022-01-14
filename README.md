# Introduction
[PyXB-X](https://github.com/renalreg/PyXB-X) is a fork of [PyXB](https://github.com/pabigot/pyxb) which aims to support Python 3.8+. The original is abandoned, and only works on Python releases upto 3.7.

One important fix that was in PyXB-X 1.2.6 was around changes to datetime in Python 3.8. This repo hosts a test case which fails on Python 3.8, but passes on 3.7.

To run this up, it is easiest to reproduce the environment using [Docker](https://www.docker.com/products/docker-desktop) (but can be done in other ways).

# Changing Python versions
Simply change the first line of the Dockerfile to be a different python version. Then re-run the below, and it'll repeat the test case on a different python version.

# Running this test case
```
$ docker compose build
$ docker compose up
```

Depending on the version of Docker you're running, you might need "docker-compose" rather than "docker compose". The former uses Compose v1, the latter is Compose v2.

# Results
Below is the output of a build after changing the first line of the Dockerfile to the relevant version, then running the test.

## Python 3.7
```
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$ docker compose build --progress quiet

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$ docker compose --ansi never up
[+] Running 1/1
 ⠿ Container pyxbx-datetime-bug-pyxbtest-1  Recreated 0.2s
Attaching to pyxbx-datetime-bug-pyxbtest-1
pyxbx-datetime-bug-pyxbtest-1  | Base python reports today + 2 months - 3 days is: 2022-03-11
pyxbx-datetime-bug-pyxbtest-1  | Last updated is: 2022-01-14 02:52:03.153892
pyxbx-datetime-bug-pyxbtest-1  | zeroDate is: 2022-03-11 00:00:00
pyxbx-datetime-bug-pyxbtest-1  | oneDate is: 2022-03-14 00:00:00
pyxbx-datetime-bug-pyxbtest-1  | twoDate is: 2022-03-11 00:00:00
pyxbx-datetime-bug-pyxbtest-1 exited with code 0
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$
```

## Python 3.8
```
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$ docker compose build --progress quiet

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$ docker compose --ansi never up
[+] Running 1/1
 ⠿ Container pyxbx-datetime-bug-pyxbtest-1  Recreated 1.6s
Attaching to pyxbx-datetime-bug-pyxbtest-1
pyxbx-datetime-bug-pyxbtest-1  | Base python reports today + 2 months - 3 days is: 2022-03-11
pyxbx-datetime-bug-pyxbtest-1  | Last updated is: 2022-01-14 02:52:54.903852
pyxbx-datetime-bug-pyxbtest-1  | zeroDate is: 2022-03-11 00:00:00
pyxbx-datetime-bug-pyxbtest-1  | oneDate is: 2022-03-14 00:00:00
pyxbx-datetime-bug-pyxbtest-1  | (2022, 3, 11, 0, 0, 0, 0, None)
pyxbx-datetime-bug-pyxbtest-1  | Traceback (most recent call last):
pyxbx-datetime-bug-pyxbtest-1  |   File "test.py", line 17, in <module>
pyxbx-datetime-bug-pyxbtest-1  |     period.twoDate = period.oneDate + relativedelta(days = -3)
pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.8/site-packages/dateutil/relativedelta.py", line 405, in __radd__
pyxbx-datetime-bug-pyxbtest-1  |     return self.__add__(other)
pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.8/site-packages/dateutil/relativedelta.py", line 387, in __add__
pyxbx-datetime-bug-pyxbtest-1  |     ret = (other.replace(**repl)
pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.8/site-packages/pyxb/binding/datatypes.py", line 687, in __new__
pyxbx-datetime-bug-pyxbtest-1  |     raise TypeError('function takes %d arguments plus optional tzinfo (%d given)' % (len(cls._ValidFields), len(args)))
pyxbx-datetime-bug-pyxbtest-1  | TypeError: function takes 3 arguments plus optional tzinfo (8 given)
pyxbx-datetime-bug-pyxbtest-1 exited with code 1
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$
```

## Python 3.9
```
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$ docker compose build --progress quiet

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$ docker compose --ansi never up
[+] Running 1/1
 ⠿ Container pyxbx-datetime-bug-pyxbtest-1  Recreated 0.1s
Attaching to pyxbx-datetime-bug-pyxbtest-1
pyxbx-datetime-bug-pyxbtest-1  | Traceback (most recent call last):
pyxbx-datetime-bug-pyxbtest-1  |   File "/test/test.py", line 17, in <module>
pyxbx-datetime-bug-pyxbtest-1  |     period.twoDate = period.oneDate + relativedelta(days = -3)
pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.9/site-packages/dateutil/relativedelta.py", line 405, in __radd__
pyxbx-datetime-bug-pyxbtest-1  |     return self.__add__(other)
pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.9/site-packages/dateutil/relativedelta.py", line 387, in __add__
pyxbx-datetime-bug-pyxbtest-1  | Base python reports today + 2 months - 3 days is: 2022-03-11
pyxbx-datetime-bug-pyxbtest-1  | Last updated is: 2022-01-14 02:53:35.234246
pyxbx-datetime-bug-pyxbtest-1  | zeroDate is: 2022-03-11 00:00:00
pyxbx-datetime-bug-pyxbtest-1  | oneDate is: 2022-03-14 00:00:00
pyxbx-datetime-bug-pyxbtest-1  | (2022, 3, 11, 0, 0, 0, 0, None)
pyxbx-datetime-bug-pyxbtest-1  |     ret = (other.replace(**repl)
pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.9/site-packages/pyxb/binding/datatypes.py", line 687, in __new__
pyxbx-datetime-bug-pyxbtest-1  |     raise TypeError('function takes %d arguments plus optional tzinfo (%d given)' % (len(cls._ValidFields), len(args)))
pyxbx-datetime-bug-pyxbtest-1  | TypeError: function takes 3 arguments plus optional tzinfo (8 given)
pyxbx-datetime-bug-pyxbtest-1 exited with code 1
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$
```

## Python 3.10
```
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$ docker compose build --progress quiet

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$ docker compose --ansi never up
[+] Running 1/1
 ⠿ Container pyxbx-datetime-bug-pyxbtest-1  Recreated 0.2s
Attaching to pyxbx-datetime-bug-pyxbtest-1
pyxbx-datetime-bug-pyxbtest-1  | Base python reports today + 2 months - 3 days is: 2022-03-11
pyxbx-datetime-bug-pyxbtest-1  | Last updated is: 2022-01-14 02:54:11.377761
pyxbx-datetime-bug-pyxbtest-1  | zeroDate is: 2022-03-11 00:00:00
pyxbx-datetime-bug-pyxbtest-1  | oneDate is: 2022-03-14 00:00:00
pyxbx-datetime-bug-pyxbtest-1  | (2022, 3, 11, 0, 0, 0, 0, None)
pyxbx-datetime-bug-pyxbtest-1  | Traceback (most recent call last):
pyxbx-datetime-bug-pyxbtest-1  |   File "/test/test.py", line 17, in <module>
pyxbx-datetime-bug-pyxbtest-1  |     period.twoDate = period.oneDate + relativedelta(days = -3)
pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.10/site-packages/dateutil/relativedelta.py", line 405, in __radd__
pyxbx-datetime-bug-pyxbtest-1  |     return self.__add__(other)
pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.10/site-packages/dateutil/relativedelta.py", line 387, in __add__
pyxbx-datetime-bug-pyxbtest-1  |     ret = (other.replace(**repl)
pyxbx-datetime-bug-pyxbtest-1  |   File "/usr/local/lib/python3.10/site-packages/pyxb/binding/datatypes.py", line 687, in __new__
pyxbx-datetime-bug-pyxbtest-1  |     raise TypeError('function takes %d arguments plus optional tzinfo (%d given)' % (len(cls._ValidFields), len(args)))
pyxbx-datetime-bug-pyxbtest-1  | TypeError: function takes 3 arguments plus optional tzinfo (8 given)
pyxbx-datetime-bug-pyxbtest-1 exited with code 1
(pyvenv-pyxbx-test) nathanr@indigo:~/work/junkcode/pyxbx-datetime-bug$
```