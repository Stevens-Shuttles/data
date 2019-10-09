import time

from lib.ShuttleService import ShuttleService, ShuttleManager


def main():
    sm = ShuttleManager(307)
    ss = ShuttleService(307)

    start_time = time.time()
    while True:
        print(f"{'ID': >10} {'Route': >40} {'Speed': >10} {'Next Stop': >30}")
        for shuttle in sm.shuttles(detailed=True):
            print("{: >10} {: >40} {: >10} {: >30}".format(
                *[shuttle.id, ss.get_route(shuttle.route_id).long_name, shuttle.speed,
                  shuttle.next_stop.name if shuttle.next_stop else "None"]))
        print()
        time.sleep(1 - ((time.time() - start_time) % 1))


if __name__ == "__main__":
    main()
