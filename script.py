import pandas as pd
from datetime import date,timedelta
import csv
import datetime
import pytz
import logging
import logging.config
from hangout_alert import alert

###################################################
model_version = 'ddi_xgboost_v1'

# Log file configuration
start_time_1=datetime.datetime.now()

zone = pytz.timezone('Asia/Calcutta')
now = datetime.datetime.now(zone)

current_hour = now.replace(minute=0, second=0, microsecond=0) - datetime.timedelta(hours=0)
current_hour_epoch = int(current_hour.timestamp())
current_hour = current_hour.strftime("%Y-%m-%d %H:%M:%S")

prediction_batch_key = str(model_version) + '_' + str(current_hour_epoch)

filename= './log/' + str(model_version) +'_'+ str(prediction_batch_key) + ".log"

def timetz(*args):
    return datetime.datetime.now(zone).timetuple()

logging.Formatter.converter = timetz
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})

logging.basicConfig(
    filename= filename,
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
###############################################################
logging.info('Script started at {}'.format(datetime.datetime.now()))

try:
    start_time = datetime.datetime.now() 
    print('Hello World')
    logging.info('Print function ran successfully in {}'.format(datetime.datetime.now()- start_time))
except Exception as e:
    logging.error('Print function failed. Error: '+str(e))

#Post alert in hangout
alert(filename)








