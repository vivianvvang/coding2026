import time
from enum import Enum
from typing import TypeVar, Generic, Callable, Optional

class RetryPolicy(Enum):
    FIXED = "FIXED"
    INCREMENTAL = "INCREMENTAL"
    EXPONENTIAL = "EXPONENTIAL"

T = TypeVar('T')

class Result(Generic[T]):
    def __init__(self, result: T, attempts: int, stopReason: str, succeeded: bool, exception: Optional[str]):
        self.result = result
        self.attempts = attempts
        self.stopReason = stopReason
        self.succeeded = succeeded
        self.exception = exception

    def getResult(self) -> T:
        return self.result

    def __str__(self) -> str:
        return f"Result: {{result={self.result}, attempts={self.attempts}, reason='{self.stopReason}', succeeded={self.succeeded}, exception={self.exception}}}"

class Retrier:
    def withRetry(self, func: Callable[[], T], maxAttempts: int, initialDelayMillis: int, policy: RetryPolicy,
                  retryOnException: Optional[Callable[[Exception], bool]], retryOnResult: Optional[Callable[[T], bool]]) -> Result[T]:
        attempt = 0
        delay = initialDelayMillis
        
        while attempt < maxAttempts:
            attempt += 1
            try:
                last_res = func()
                # Check if the result itself should trigger a retry
                if retryOnResult is not None and retryOnResult(last_res):
                    if attempt < maxAttempts:
                        self.sleep(delay)
                        delay = self.nextDelay(initialDelayMillis, policy, attempt)
                        # Go to next iteration
                else:
                    return Result(last_res, attempt, "Success", True, None)

            except Exception as e:
               
                if retryOnException is not None and retryOnException(e): 
                    if attempt < maxAttempts:
                        self.sleep(delay)
                        delay = self.nextDelay(initialDelayMillis, policy, attempt)
                else:
                    # Exception is not retryable
                    return Result(None, attempt, "Exception not retryable", False, str(e))
        
        # loop finishes, exhasted all attemps
        return Result(
            result = None,
            attempts = attempt,
            stopReason = "Max attemps reached",
            succeeded = False,
            exception = None
        )
    
    @staticmethod
    def sleep(ms: int):
        try:
            time.sleep(ms / 1000.0)
        except:
            pass

    @staticmethod
    def nextDelay(initial: int, policy: RetryPolicy, attempt: int) -> int:
        if policy == RetryPolicy.FIXED:
            return initial
        elif policy == RetryPolicy.INCREMENTAL:
            return initial * (attempt + 1)
        elif policy == RetryPolicy.EXPONENTIAL:
            return initial * (1 << attempt)
        else:
            return initial

if __name__ == "__main__":
    print("======= Test 1: Success on first try ======")
    result1 = Retrier().withRetry(lambda: "Success", 3, 100, RetryPolicy.FIXED, lambda e: True,
                                  lambda r: False)
    print(result1)

    print("\n======= Test 2: Always fails (incremental delay) ======")
    def always_fail():
        raise RuntimeError("Always fail")
    result2 = Retrier().withRetry(always_fail, 4, 50, RetryPolicy.INCREMENTAL, lambda e: True, lambda r: False)
    print(result2)

    print("\n======= Test 3: Succeeds on 5th attempt (exponential backoff) ======")
    cnt = [0]
    def succeed_on_fifth():
        cnt[0] += 1
        if cnt[0] < 5:
            raise RuntimeError(f"Fail{cnt[0]}")
        return f"Ok at attempt {cnt[0]}"
    result3 = Retrier().withRetry(succeed_on_fifth, 5, 50, RetryPolicy.EXPONENTIAL, lambda e: True, lambda r: False)
    print(result3)

    print("\n======= Test 4: Retry on result (fixed delay) ======")
    tries = [0]
    def increment_tries():
        tries[0] += 1
        return tries[0]
    result4 = Retrier().withRetry(increment_tries, 10, 80, RetryPolicy.FIXED, lambda e: True,
                                  lambda r: r < 5)
    print(result4)  # Should stop when tries equals to 5

    print("\n======= Test 5: No retry on exception  (fixed delay) ======")
    def fail_on_first():
        raise RuntimeError("Fail on first attempt")
    result5 = Retrier().withRetry(fail_on_first, 3, 100, RetryPolicy.FIXED, lambda e: False, lambda r: False)
    print(result5)