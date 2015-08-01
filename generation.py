__author__ = 'JuanJose'

import datetime
import threading
import copy

full = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'
        's', 't', 'u', 'v', 'x', 'y', 'z'
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
my = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
      'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
mn = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
      's', 't', 'u', 'v', 'x', 'y', 'z']
nm = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

dist = []
iterations = [0]
finish = [0]
threads = []
lock = threading.Lock()
time = [0]
for i in range(0, 8):
    dist.append([])

dist[0] = my
dist[1] = mn
dist[2] = mn
dist[3] = mn
dist[4] = mn
dist[5] = mn
dist[6] = nm
dist[7] = nm

cases = 1

for k in dist:
    cases *= len(k)

print 'the number of cases are: ', cases

def rec(index, word):
    if len(word) == 8:
        found(word)
    if finish[0] == 0:
        #create threads in this case
        if len(word) == 0 or len(word) == 1:
            for i in dist[index]:
                n = ''.join([word, i])
                n_word = copy.deepcopy(n)
                t = threading.Thread(target=rec, args=(index+1, n_word))
                threads.append(t)
                t.start()
        else:
            #Add other letter
            if index < len(dist):
                for j in dist[index]:
                    n = ''.join([word, j])
                    n_word = copy.deepcopy(n)
                    rec(index+1, n_word)


def found(word):
    #lock.acquire()
    iterations[0] += 1
    if iterations[0] % 1000000 == 0:
        print iterations[0] / 1000000, 'M'
        print word
        print 'threads: ', len(threads)
    #lock.release()
    if word == 'Blabla78':
        finish[0] = 1
        print 'found it'
        print 'iteration: ', iterations[0]
        time2 = datetime.datetime.now() - time[0]
        print 'Completion time: ', time2

time[0] = datetime.datetime.now()
rec(0, '')
time1 = datetime.datetime.now() - time[0]
print 'First Thread time: ', time1
