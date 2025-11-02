import time

from functools import wraps

from fastapi import HTTPException, Request,status

def rate_limited(max_calls:int,time_frame: int):
    """
    Simple in-memory rate limiter decorator.
    Applies per-endpoint restriction.

    Args:
        max_calls (int): maximum calls
        time_frame (int): under timeframe 
    """

    def decorator(func):

        # store time stamps for recent calls for this specific endpoints
        calls=[]

        @wraps(func)
        async def wrapper(request: Request,*args,**kwargs):
            now=time.time()

            # keep only timestamps within the time window

            calls_in_time_frame=[call for call in calls if call >=now-time_frame]

            # greater or equal .. equal is considered as if the current one is 
            # appened then it will be greater than max_calls
            if(len(calls_in_time_frame)>=max_calls):
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Rate limit exceeded."
                )
        

            # record the current call

            calls.append(now)

            # retain only the last max_calls for next check
            # atleast max_calls number time stamp should have to be for checking

            if(len(calls)>max_calls):
                del calls[:-max_calls]
            
            # proceed with the orginal route function

            return await func(request,*args,*kwargs)
        

        return wrapper
    
    return decorator
                



