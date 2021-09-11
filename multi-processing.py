from multiprocessing import Process, cpu_count
import time

def count(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count())

    a = Process(target=count, args=(62500000,))
    b = Process(target=count, args=(62500000,))
    c = Process(target=count, args=(62500000,))
    d = Process(target=count, args=(62500000,))
    e = Process(target=count, args=(62500000,))
    f = Process(target=count, args=(62500000,))
    g = Process(target=count, args=(62500000,))
    h = Process(target=count, args=(62500000,))
    i = Process(target=count, args=(62500000,))
    j = Process(target=count, args=(62500000,))
    k = Process(target=count, args=(62500000,))
    l = Process(target=count, args=(62500000,))
    m = Process(target=count, args=(62500000,))
    n = Process(target=count, args=(62500000,))
    o = Process(target=count, args=(62500000,))
    p = Process(target=count, args=(62500000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()
    m.start()
    n.start()
    o.start()
    p.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    i.join()
    j.join()
    k.join()
    l.join()
    m.join()
    n.join()
    o.join()
    p.join()

    print(time.perf_counter())
if __name__ == "__main__":
    main()