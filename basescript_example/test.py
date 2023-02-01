from basescript import BaseScript
import time
import random

class Stats(BaseScript):
    def __init__(self):
        super(Stats, self).__init__()

    def run(self):
        ts = time.time()
        while True:
            # Metric Format.
            self.log.info("stats", time_duration=(time.time()-ts), type="metric", random_number=random.randint(1, 50))

if __name__ == '__main__':
    Stats().start()