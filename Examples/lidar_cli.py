import PyLidar3
import time


if __name__ == "__main__":

    port = "/dev/cu.usbserial-0001"
    obj = PyLidar3.YdLidarG4(port) #PyLidar3.your_version_of_lidar(port,chunk_size)
    time_duration = 200

    if(obj.Connect()):
        try:
            print(obj.GetDeviceInfo())
            gen = obj.StartScanning()
            t = time.time() # start time 
            while (time.time() - t) < time_duration: #scan for 30 seconds
                print(next(gen))   
        except KeyboardInterrupt:
            print("\nProgram is stopped by user")
            obj.StopScanning()
            obj.Disconnect()
    else:
        print("Error connecting to device")
