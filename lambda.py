import time

import boto3

from Transloc.ShuttleService import ShuttleService, ShuttleManager


sm = ShuttleManager(307)
    
dynamodb = boto3.resource("dynamodb")
    
table = dynamodb.Table("shuttles")


def handler(event, context):    
    start_time = time.time()
    with table.batch_writer(overwrite_by_pkeys=["id", "timestamp"]) as writer:
        for _ in range(5):
            for shuttle in sm.shuttles():
                # print(shuttle.as_serializable_dict())
                writer.put_item(Item = shuttle.as_serializable_dict())
            time.sleep(1 - ((time.time() - start_time) % 1))


if __name__ == "__main__":
    handler(None, None)

