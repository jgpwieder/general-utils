import traceback
from time import time, sleep


def retry(timeout=None, limit=None, constant=None, coefficient=None, maxWait=None):
    limit = limit or 0
    timeout = timeout or 0
    maxWait = maxWait or 5
    constant = constant or 0.015
    coefficient = coefficient or 1.7

    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            since = time()
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as exception:  # TODO: Chose exception to retry on input
                    attempt += 1
                    elapsed = time() - since

                    maxSleepTime = min(timeout - elapsed, maxWait) if timeout else maxWait
                    sleepTime = min(constant * (coefficient ** attempt), maxSleepTime)
                    nextAttempt = time() + sleepTime

                    isExpired = False
                    if timeout and (nextAttempt - since) >= timeout:
                        isExpired = True
                    if limit and attempt >= limit:
                        isExpired = True

                    print("ERROR: Retry attempt {attempt}\n sleep {sleepTime}s\n exception: {exception}\n traceback: {traceback}".format(
                        attempt=attempt,
                        sleepTime=sleepTime,
                        exception=str(exception),
                        traceback=traceback.format_exc(),
                    ))
                    if isExpired:
                        raise exception

                    sleep(sleepTime)

        return wrapper
    return decorator
