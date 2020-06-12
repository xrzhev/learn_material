import socket
import logging
import threading
import os


logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(asctime)s %(threadName)s : %(message)s")

LISTEN_NUM = 100

logging.info("Application is runnning...")
logging.debug("NUMBER OF PORTS: {0}".format(LISTEN_NUM))


class sock_con:
    def __init__(self, is_fake, logging):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("0.0.0.0", 0))
        self.sock.listen()

        self.logging = logging
        self.is_fake = is_fake
        self.info = {
                "port":self.sock.getsockname()[1],
        }

        self.loopth = threading.Thread(target=self.main_loop, name="port:{}".format(self.info["port"]))
        self.loopth.start()


    def main_loop(self):
        self.logging.debug("started")
        if self.is_fake == False:
            self.logging.critical("CORRECT PORT!")
        while(1):
            con, addr = self.sock.accept()
            thread = threading.Thread(target=self.listener,args=(con, addr), name="listener-port:{}".format(self.info["port"]))
            thread.start()


    def listener(self, con, addr):
        self.logging.info("{0} is connected".format(addr[0]))

        if self.is_fake == True:
            con.sendall(b"incorrect. try harder!\n")

        if self.is_fake == False:
            con.sendall(b"correct!\n")
            con.sendall(b"Give you a Shell...\n")
            self.logging.warn("{0} in Shell!".format(addr[0]))
            while(1):
                con.sendall(b"$ ")
                user_input = con.recv(1024).decode()
                v = os.popen(user_input).read()
                con.sendall(v.encode())

        con.close()
        self.logging.info("{0} is disconnected.".format(addr[0]))


if __name__ == "__main__":
    hoge = []
    for i in range(LISTEN_NUM-1):
        hoge.append(sock_con(True , logging))
    hoge.append(sock_con(False, logging))
