__author__ = 'JuanJose'

import datetime
import threading

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
lock = threading.Lock()

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

def rec(index, word):
    if len(word) == 8:
        found(word)
    if finish[0] == 0:
        if index < len(dist):
            for i in dist[index]:
                n_word = ''.join([word, i])
                t = threading.Thread(target=rec, args=(index+1, n_word))
                t.run()
        else:
            return word

def found(word):
    #lock.acquire()
    iterations[0] += 1
    if iterations[0] % 1000000 == 0:
        print iterations[0] / 1000000, 'M'
        print word
    #lock.release()
    if word == 'Blabla78':
        finish[0] = 1
        print 'found it'
        print 'iteration: ' + iterations

    return 0

time = datetime.datetime.now()
rec(0, '')
time = time - datetime.datetime.now()
print time
