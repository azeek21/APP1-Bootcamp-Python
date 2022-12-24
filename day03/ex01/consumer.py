import redis
import json
from logging import info, error, debug
import logging
import argparse


logging.basicConfig(level=logging.INFO, format="%(message)s")

bad_guys_accs = []

def listener(red: redis.Redis):
    info("Connecting channel to listen updates ...")
    try:
        subscriber = red.pubsub()
        subscriber.subscribe("transactions")
    except Exception as e:
        error(e)
        return False
    info("Cennection success")

    info("Listening updates ....")
    for msg in subscriber.listen():
        if msg is not None:
            if msg.get('type') == 'message':
                fixer(msg.get('data'))

    return True

def fixer(message: str):

    global bad_guys_accs

    try:
        load:dict = json.loads(message)
    except:
        error("Can't load message to json object ...")
        return False

    sender = load.get('metadata').get('from')
    receiver = load.get('metadata').get('to')
    amount = load.get('amount')
 
    if amount > 0 and receiver in bad_guys_accs:
        load['metadata']['from']  = receiver
        load['metadata']['to'] = sender

    info(str(load))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", help= "list of bad guys' account numbers, lengt = 10")
    args = parser.parse_args()
    if args.e:
        baddies = args.e
        baddies = baddies.split(',')
        for i in baddies:
            if i.isdigit():
                bad_guys_accs.append(int(i))
            else:
                error("Account numbes of bad guys should be all numeric\nE.g: 1111111111,2222222222")
                exit(1)
    else:
        info("Bad guts' accounts not specified, using default 2222222222,444444444")
        bad_guys_accs = [2222222222,4444444444]


    info("Redis connecting ...")
    try:
        red = redis.StrictRedis('localhost', 6379, decode_responses=True)
        info("Redis connection success !")
    except:
        info("Redis connection fail !")
        error("Something went wrong")
        exit(1)


    while listener(red):
        pass
