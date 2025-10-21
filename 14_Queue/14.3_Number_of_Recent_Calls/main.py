# Number of Recent Calls
# Topic: Queue
# Type: Home Challenge

from collections import deque

class RecentCounter:
    def __init__(self):
        # Initialize queue
        pass

    def ping(self, t: int) -> int:
        # Add t, remove old requests, return count
        pass

# Demo
if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))    
    print(rc.ping(100))  
    print(rc.ping(3001)) 
    print(rc.ping(3002))
