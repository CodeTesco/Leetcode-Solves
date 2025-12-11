class RecentCounter:

    def __init__(self):
        self.requests = []
    
    def ping(self, t):
        self.requests.append(t)
        while True:
            diff = abs(t - self.requests[0])
            if diff > 3000:
                self.requests = self.requests[1:]
            else:
                break
        
        return len(self.requests)
    
obj = RecentCounter()
obj.ping(1)
obj.ping(2)
obj.ping(100)
obj.ping(3001)
param1 = obj.ping(3002)
print(param1)