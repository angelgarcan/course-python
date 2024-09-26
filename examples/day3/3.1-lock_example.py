import logging
from multiprocessing import Lock


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d|%(levelname)s|%(message)s',
                        datefmt='%Y-%m-%dT%H:%M:%S')

    chopstick = Lock()

    ################# PHILOSOPHER 1
    logging.info(f"P1: acquiring chopstick")
    if chopstick.acquire():
        logging.info(f"P1: chopstick acquired by me")
    else:
        logging.info(f"P1: chopstick is in use")


    ################# PHILOSOPHER 2
    logging.info(f"P2: acquiring chopstick (wating 5 seconds)")
    if chopstick.acquire(timeout=5): # Timeout to not wait for the eternity
        logging.info(f"P2: chopstick acquired by me")
    else:
        logging.info(f"P2: chopstick is in use")


    ################# PHILOSOPHER 1
    logging.info("P1: releasing chopstick")
    chopstick.release()

    ################# PHILOSOPHER 2
    logging.info(f"P2: acquiring chopstick")
    if chopstick.acquire():
        logging.info(f"P2: chopstick acquired by me")
    else:
        logging.info(f"P2: chopstick is in use")

    logging.info("P2: releasing chopstick")
    chopstick.release()

    logging.info("DONE !!!")
