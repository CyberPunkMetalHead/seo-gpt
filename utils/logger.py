import logging
from datetime import datetime

logging.basicConfig(
    filename=f"logs/{datetime.today().strftime('%Y-%m-%d')}_log.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)
