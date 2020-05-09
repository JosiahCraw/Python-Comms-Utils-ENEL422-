import os
import threading
from typing import List
import comms_utils.psd as psd
import numpy as np

def run_sy(sy, x: List[float], rc: List[List[float]], rc_lock, thread_id: int):
    output = list()
    print('thread: {} started'.format(thread_id))
    for val in x:
        output.append(sy[float(val)])
    with rc_lock:
        print('thread: {} finished'.format(thread_id))
        rc[thread_id] = output

def sy(sy, x: List[float]) -> List[float]:
    num_threads = os.cpu_count()
    threads = list()
    rc = [[0.0]] * num_threads
    rc_lock = threading.Lock()
    x_split = np.array_split(x, num_threads)
    thread_id = 0
    for sub_x in x_split:
        thread = threading.Thread(None, run_sy, args=[sy, sub_x, rc, rc_lock, thread_id])
        threads.append(thread)
        thread_id += 1
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    output = list()
    for item in rc:
        output.extend(item)
    return output