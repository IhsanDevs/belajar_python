from collections import deque

antrian = deque([1,2,3,4,5,6,7])
print("Data sekarang: ", antrian)

out = antrian.popleft()
print(antrian)
print(out)