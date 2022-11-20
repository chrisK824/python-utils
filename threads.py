import threading
from time import sleep
from datetime import datetime
from sys import stdout


def dummy_loop(barrier, event, minutes=1, step_in_seconds=5):
    """Starts a dummy loop to run for certain minutes given
    Prints the thread of execution every given amount of seconds"""
    thread = threading.current_thread().name
    print(f"Thread \"{thread}\" triggered at {datetime.now()} waiting for all to trigger")
    # this thread of execution will wait for the barrier to be broken 
    # so that it can continue
    barrier.wait()
    steps = minutes*60/step_in_seconds
    while steps > 0:
        remain_time = steps*step_in_seconds
        event.wait()
        print(f"Seconds left for thread \"{thread}\": {remain_time} seconds -- Going to sleep.")
        steps = steps - 1
        sleep(step_in_seconds)
    print(f"Thread \"{thread}\" expired at {datetime.now()}")

def create_threads(barrier, event, threads_to_spawn=10):
    """Creates a number of threads to spawn"""
    thread_pool = []
    for i in range(0, threads_to_spawn):
        thread_to_create = threading.Thread(target=dummy_loop, name=f"Dummy loop-{i}", args=(barrier, event, 0.5, 1))
        thread_pool.append(thread_to_create)
    return thread_pool


def run_threads(thread_pool_to_run, distance_in_seconds=None):
    """Starts every thread in a given pool with a distance of seconds in between"""
    for thread in thread_pool_to_run:
        thread.start()
        if distance_in_seconds:
            sleep(distance_in_seconds)


if __name__ == '__main__':
    print("Starting thread executions")
    print("Current number of threads: " + str(threading.active_count()))
    barrier_limit = 5
    # Create an event to pass in all threads
    event = threading.Event()
    # create a barrier for a limit of waiting threads
    barrier = threading.Barrier(barrier_limit)
    # create a number of threads to equal the barrier
    # this will result to trigger the wait function for all of them, as main
    # thread adds always 1 to the total threads
    pool = create_threads(barrier, event, barrier_limit)
    # start all the threads by an interval in seconds
    run_threads(pool)
    print("Current number of threads: " + str(threading.active_count()))
    print("Threads have broken the barrier but still are holding by an event wait")
    sleep(5)

    while threading.active_count() > 1:
        print("Let's release them")
        event.set()
        sleep(5)
        print("Ok hold on a bit !")
        event.clear()
        sleep(5)
