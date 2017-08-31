import datetime

import pytz

utc = pytz.utc
ist = pytz.timezone('America/Sao_Paulo')

now = datetime.datetime.now(tz=utc)
ist_now = now.astimezone(ist)
print ist_now