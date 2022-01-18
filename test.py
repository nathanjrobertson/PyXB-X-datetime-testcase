from datetime import datetime, date, timedelta
from wsgiref.simple_server import sys_version
from dateutil.relativedelta import relativedelta
import sys

from generated import protocol

print("Python version is: {}.{}".format(sys.version_info[0], sys.version_info[1]))

# This does not fail. It doesn't hit PyXB code. However, it is equivalent.
equivalent_base_python_test = date.today() + relativedelta(months = + 2) + relativedelta(days = -3)
print("Base python reports today + 2 months - 3 days is: {}".format(equivalent_base_python_test))

period = protocol.someType()
period.lastUpdated = datetime.now()
print("Last updated is: {} (type {}, module {})".format(period.lastUpdated, type(period.lastUpdated).__name__, type(period.lastUpdated).__module__))
period.zeroDate = date.today() + relativedelta(months = + 2) + relativedelta(days = -3)
print("zeroDate is: {} (type {}, module {})".format(period.zeroDate, type(period.zeroDate).__name__, type(period.zeroDate).__module__))
period.oneDate = date.today() + relativedelta(months = + 2)
print("oneDate is: {} (type {}, module {})".format(period.oneDate, type(period.oneDate).__name__, type(period.oneDate).__module__))
period.twoDate = period.oneDate + relativedelta(days = -3)
print("twoDate is: {} (type {}, module {})".format(period.twoDate, type(period.twoDate).__name__, type(period.twoDate).__module__))
