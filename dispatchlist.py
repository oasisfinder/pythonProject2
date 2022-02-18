import os
from datetime import datetime
start = datetime.today().replace(day=1).strftime("%Y.%m.%d")
end = datetime.today().strftime("%Y.%m.%d")
os.system("main.vbs {} {}".format(start, end))