import json
import redis
from logging import info, debug, warning, error, critical
import logging
from random import randint

logging.basicConfig(level=logging.INFO, format="%(message)s")


def send_message(red: redis.Redis):
    info("Generating message ...")
 
    from_peer = randint(1000000000, 9999999999)
    to_peer = randint(1000000000, 9999999999)
    amout = randint(-9999, 99999)
 
    debug(f"MESSAGE DETAILS:\n\tfrom: {from_peer}\n\tto: {to_peer}\n\tamount: {amout}")

    message = {
        "metadata":
        {
            "from": from_peer,
            "to": to_peer,
        },
        "amount": amout
        }

    message = json.dumps(message)

    debug("MESSAGE to JSON SUCCESSFUL")

    info("Message ready to send ...")
    try:
        red.publish('transactions', message)
        info("Message sent sucessfully.\n")
    except Exception as e:
        info("Message not sent, something wrong ...")
        error(e)
        
def default_test(red: redis.Redis):
        messages: list = [
            {"metadata": {"from": 1111111111,"to": 2222222222},"amount": 10000},
            {"metadata": {"from": 3333333333,"to": 4444444444},"amount": -3000},
            {"metadata": {"from": 2222222222,"to": 5555555555},"amount": 5000},
        ]

        messages = [json.dumps(i) for i in messages]

        for i in messages:
            try:
                red.publish('transactions', i)
                info("Message sent sucessfully.\n")
            except Exception as e:
                info("Message not sent, something wrong ...")
                error(e)



if __name__ == "__main__":
    info("REDIS CONNECTING ...")

    try:
        red = redis.StrictRedis("localhost", 6379, charset='utf-8', decode_responses=True)
        info("REDISS CONNECION SUCCESS ...")
    except Exception as e:
        info("FATALL, something wrong with redis connection")
        error(e)

    # send_message(red)
    default_test(red)
