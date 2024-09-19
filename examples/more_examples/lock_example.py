import logging
from multiprocessing import Lock


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d|%(levelname)s|%(message)s',
                        datefmt='%Y-%m-%dT%H:%M:%S')

    chopstick = Lock()

    logging.info("acquire 1")
    logging.info(chopstick.acquire())

    logging.info("acquire 2")
    logging.info(chopstick.acquire(timeout=1))

    logging.info("relase 1")
    chopstick.release()

    # logging.info("relase 2")
    # chopstick.release()

    logging.info("DONE !!!")
