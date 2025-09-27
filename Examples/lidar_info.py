import PyLidar3
import time


if __name__ == "__main__":

    port = "/dev/ttyUSB0"
    obj = PyLidar3.YdLidarG4(port) #PyLidar3.your_version_of_lidar(port,chunk_size)

    if(obj.Connect()):
        try:
            print(obj.GetDeviceInfo())
            print("Current Frequency: " + str(obj.GetCurrentFrequency()) + " Hz")
            print("Current Ranging Frequency: " + str(obj.GetCurrentRangingFrequency()) + " kHz")
            print("Health Status: " + str(obj.GetHealthStatus()))
            obj.Disconnect()
        except Exception as e:
            print("\nError occurred: " + str(e))
    else:
        print("Error connecting to device")
