from confluent_kafka import Producer

class ProducerContextManager:
    def __init__(self, config):
        self.config = config
        self.producer = None

    def __enter__(self):
        self.producer = Producer(self.config)
        return self.producer

    def __exit__(self):
        if self.producer:
            self.producer.flush()