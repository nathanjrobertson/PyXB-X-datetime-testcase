from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

from generated import protocol

# This does not fail. It doesn't hit PyXB code. However, it is equivalent.
equivalent_base_python_test = date.today() + relativedelta(months = + 2) + relativedelta(days = -3)
print("Base python reports today + 2 months - 3 days is: {}".format(equivalent_base_python_test))

period = protocol.someType()
period.lastUpdated = datetime.now()
print("Last updated is: {}".format(period.lastUpdated))
period.zeroDate = date.today() + relativedelta(months = + 2) + relativedelta(days = -3)
print("zeroDate is: {}".format(period.zeroDate))
period.oneDate = date.today() + relativedelta(months = + 2)
print("oneDate is: {}".format(period.oneDate))
period.twoDate = period.oneDate + relativedelta(days = -3)
print("twoDate is: {}".format(period.twoDate))
