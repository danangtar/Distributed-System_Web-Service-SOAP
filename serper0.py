from ladon.ladonizer import ladonize
import pickle
import os

class buut(object):

    @ladonize(rtype=str)
    def kerja(self):
        filenya = os.listdir("../filenya/.")
        listnya = filenya[((len(filenya)/2)-1):]

        sentence = {}

        for files in listnya:
            print files
            for line in open("../filenya/"+files).xreadlines():
                cek = line.split()
                cek = " ".join(cek[4:])

                if (cek in sentence):
                    sentence[cek] += 1
                else:
                    sentence[cek] = 0

        sort = sorted(sentence.items(), key=lambda x:x[1], reverse=True)
        sort = pickle.dumps(sort)
        return sort
