from dotenv import load_dotenv
import os
load_dotenv()

config = {
        # User-specific properties that you must set
        'bootstrap.servers': os.getenv('BOOTSTRAP_SERVER'),
        'sasl.username':     os.getenv('CLUSTERAPIKEY'),
        'sasl.password':     os.getenv('CLUSTERAPISECRET'),

        # Fixed properties
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms':   'PLAIN',
        'group.id':          'kafka-python-getting-started',
        'auto.offset.reset': 'earliest'
}
