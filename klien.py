from suds.client import Client
import pickle
import time

tstart = time.time()

client1 = Client('http://localhost:5001/buut')
client2 = Client('http://localhost:5002/buut')

hasil1 = client1.service.kerja()
hasil1 = pickle.loads(hasil1)

hasil2 = client2.service.kerja()
hasil2 = pickle.loads(hasil2)
hasil2 = dict((x, y) for x, y in hasil2)

for freq in hasil1:
    if freq[0] in hasil2:
        hasil2[freq[0]] = hasil2[freq[0]] + freq[1]
    else:
        hasil2[freq[0]] = freq[1]

hasil2 = sorted(hasil2.items(), key=lambda x: x[1], reverse=True)

i = 0
while i < 10:
    print hasil2[i]
    i = i + 1

tend = time.time()
print("Total elapsed time: %d msec" % ((tend-tstart)*1000))