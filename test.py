import time

from Transloc.ShuttleService import ShuttleService, ShuttleManager


def main():
    # A ShuttleManager is basically an auto-updating list of Shuttles
    sm = ShuttleManager(307)
    # A ShuttleService is how we access the API
    ss = ShuttleService(307)

    start_time = time.time()
    while True:
        # The >10, >40, etc. say to format the columns with that number of spaces
        print(f"{'ID': >10} {'Route': >40} {'Speed': >10} {'Next Stop': >30}")

        # Need to print the data for each shuttle that the ShuttleManager gives us when we call sh.shuttles()
        # detailed=True fetches additional information about the shuttle at the expense of extra web requests
        for shuttle in sm.shuttles(detailed=True):
            # Use the same formatting as the previous print
            print("{: >10} {: >40} {: >10} {: >30}".format(
                shuttle.id, ss.get_route(shuttle.route_id).long_name, shuttle.speed,
                shuttle.next_stop.name if shuttle.next_stop else "None")
            )
        print()
        # Since we want the loop to be once every 2 seconds, we need to sleep for 2 seconds minus the amount of time
        # spent running the code in the loop, otherwise we will drift.
        time.sleep(2 - ((time.time() - start_time) % 2))


if __name__ == "__main__":
    main()
