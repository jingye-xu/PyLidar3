import threading
import PyLidar3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from threading import Thread
import math    
import time
import numpy as np


def all_realtime_animation():
    fig, ax = plt.subplots(nrows=1, figsize=(7,7))
    gap_size = 500

    global x
    global y

    def animate(i):
        # mirrored by line: y=-x
        x_plot = -y
        y_plot = -x
        ax.clear()
        ax.set_ylim(min(y_plot)-gap_size,max(y_plot)+gap_size)
        ax.set_xlim(min(x_plot)-gap_size,max(x_plot)+gap_size)
        ax.scatter(x_plot, y_plot, c='r', s=8)

    ani = animation.FuncAnimation(fig, animate, interval=4)
    plt.show()
    

def data_fetch(Obj):
    if(Obj.Connect()):
        print(Obj.GetDeviceInfo())
        gen = Obj.StartScanning()
        global is_run
        while is_run:
            data = next(gen)
            process_start = time.time()
            for angle in range(0,360):
                # if(data[angle]>1000):
                x[angle] = data[angle] * math.cos(math.radians(angle))
                y[angle] = data[angle] * math.sin(math.radians(angle))
            process_end = time.time()
            print(f"process time: {process_end - process_start:.6f} s")
        
        print("stopping lidar...", end="")
        obj.StopScanning()
        obj.Disconnect()
        print("done.")
    else:
        print("Error connecting to device")


if __name__ == "__main__":
    x= np.array([0 for _ in range(360)])
    y= np.array([0 for _ in range(360)])
    is_run = True
    
    port = "/dev/cu.usbserial-0001"
    obj = PyLidar3.YdLidarG4(port)
    thread_data = Thread(target=data_fetch, args=(obj,), daemon=False)
    thread_data.start()

    try:
        all_realtime_animation()
    except KeyboardInterrupt:
        print("\nkeyboard interrupted")
        plt.close("all")
    finally:
        is_run = False
        thread_data.join()
        print("main program finished")
