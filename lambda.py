import time

import boto3

from Transloc.ShuttleService import ShuttleService, ShuttleManager


def handler(event, context):
    # A ShuttleManager is basically an auto-updating list of Shuttles
    sm = ShuttleManager(307)

    batch = []
    start_time = time.time()
    for _ in range(5):
        for shuttle in sm.shuttles():
            batch.append(shuttle.as_serializable_dict())
        time.sleep(2 - ((time.time() - start_time) % 2))

    # TODO upload to DynamoDB and deal with the fact that duplicate Shuttle ID + timestamp combos can be received
    pass


if __name__ == "__main__":
    handler(None, None)
