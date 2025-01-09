import json
import logging
from pprint import pformat
from dotenv import load_dotenv
import os
load_dotenv()

def stat_handler(stats_msg: str) -> None:
    stats = json.loads(stats_msg)
    logging.info("STATS: %s", pformat(stats))

kafka_producer_config = {
        # User-specific properties that you must set
        'bootstrap.servers': os.getenv('BOOTSTRAP_SERVER'),
        'sasl.username':     os.getenv('CLUSTERAPIKEY'),
        'sasl.password':     os.getenv('CLUSTERAPISECRET'),

        # Fixed properties
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms':   'PLAIN',
        'group.id':          'kafka-python-getting-started',
        'auto.offset.reset': 'earliest',
        "statistics.interval.ms": 3 * 1000,
        "stats_cb": stat_handler,
        "debug": "msg",
        "linger.ms": 200,
        "compression.type": "gzip",
}
