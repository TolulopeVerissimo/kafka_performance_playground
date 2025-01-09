import json
import logging
from producer import ProducerContextManager
from pprint import pformat
from config.kafka_producer_config import kafka_producer_config
from requests_sse import EventSource

def callback(err, event):
    if err:
        print(f'Produce to topic {event.topic()} failed for event: {event.key()}')
    else:
        val = event.value().decode('utf8')
        print(f'{val} sent to partition {event.partition()}.')
        

def main():
    logging.info('Start')

    producer = ProducerContextManager(kafka_producer_config)
    with (
        producer as p,
        EventSource(
        'http://github-firehose.libraries.io/events',
        timeout=30
    ) as event_source):
        for event in event_source:
            value = json.loads(event.data)
            key = value['id']
            logging.info("Got: %s", pformat(value))

            p.produce('github_events', key=key, value=json.dumps(value), on_delivery=callback)
            p.flush()


if __name__ == '__main__':
    try:
        logging.basicConfig(level='INFO')
        main()
    except KeyboardInterrupt:
        pass