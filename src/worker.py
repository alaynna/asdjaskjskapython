
from threading import Thread
import time

class worker(Thread):

    def __init__(
        self,
        clientSocket,
        interval,
        filePath,
        ):
        self.clientSocket = clientSocket
        self.interval = interval
        self.filePath = filePath
        Thread.__init__(self)

    def run(self):
        startofsegment = False
        output = ''
        f = open(self.filePath, 'r')
        for x in f:

            # package start with &&

            if x == '&&\n':
                startofsegment = True
                output = ''

            output = output + x

            # package end with !! and complete package start with && end with !!

            if x == '!!\n' and startofsegment:
                startofsegment = False
                self.clientSocket.send(output.encode())
                print(output)
                time.sleep(1)
                output = ''
            elif x == '!!\n':
                startofsegment = False
                output = ''

        f.close()
        self.clientSocket.close()


   