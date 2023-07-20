from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(forecastApi.update_forecast, 'interval', minutes=5)
    # scheduler.start()