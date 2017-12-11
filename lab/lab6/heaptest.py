import heapq

q = []

heapq.heappush(q,(2,'code'))
heapq.heappush(q,(1,'eat'))
heapq.heappush(q,(3,'sleep'))

print("first is ")
print(q[0]) 

print("each item:")
for item in q:
    print item

while q:
    next_item = heapq.heappop(q)
    print(next_item)