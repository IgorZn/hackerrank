import os, time


def counter(count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), i))


if __name__ == '__main__':
    for i in range(5):
        pid = os.fork()
        if pid != 0:
            print('Proccess %d spawned. Parent pid is: %s' % (pid, os.getpid()))
        else:
            counter(5)
            os._exit(0)
    print('Main process exiting.')