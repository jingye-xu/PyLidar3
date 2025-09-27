# PyLidar3

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/lakshmanmallidi/PyLidar3) [![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/lakshmanmallidi/PyLidar3/License)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Flakshmanmallidi%2FPyLidar3.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Flakshmanmallidi%2FPyLidar3?ref=badge_shield)
<br />PyLidar3 is python 3 package to get data from Lidar device. Currently supports ydlidar from [https://www.ydlidar.com](http://www.ydlidar.com).

## Source code
Source code is available on github's repository. <br />
[https://github.com/lakshmanmallidi/PyLidar3/blob/master/PyLidar3/\__init.py\_\_](https://github.com/lakshmanmallidi/PyLidar3/blob/master/PyLidar3/__init__.py)

## Dependencies
* pyserial
* time
* math
* enum

## Installation

##### Using Pip
```
pip install PyLidar3
```
You can also install using setup.py file from git repository.

## Usage
This package consists of multiple classes representing the version of lidar you are using. The class structure is YdLidarX4 where X4 is version name ydlidar. Further contribution are actively accepted. 
##### Class structure:
###### YdLidarX4
`Arguments`: port, chunk_size(default:6000).<br/>

`port`: serial port to which device is connected. Example: com4, /dev/ttyAMC0.<br/>

`chunk_size`: Number of bytes of data read from device. Increase in chunk_size results in more averaged angle:distance pairs but increase response time result in slower data acquisition. For faster data acquisition decrease chunk_size.<br/>
```
Note: Calibrate chunk size depends on your application and frequency of device. 
if the chunk size is not enough not all angles are covered. 
```

* `Connect` -- Begin serial connection with Lidar by opening serial port. Return success status True/False.<br />

* `StartScanning` -- Begin the lidar and returns a generator which returns a dictionary consisting angle(degrees) and distance(millimeters).<br />
 `Return Format` : {angle(0):distance, angle(2):distance,....................,angle(359):distance}<br />

* `StopScanning` -- Stops scanning but keeps serial connection alive.<br />

* `GetHealthStatus` -- Returns True if Health of lidar is good else returns False<br />

* `GetDeviceInfo` -- Returns Information of Lidar version, serial number etc.<br />

* `Reset` -- Reboot the lidar <br />

* `Disconnect` -- Stop scanning and close serial communication with Lidar. <br />

###### YdLidarG4
`Arguments`: port, chunk_size(default:6000).<br/>

`port`: serial port to which device is connected. Example: com4, /dev/ttyAMC0.<br/>

`chunk_size`: Number of bytes of data read from device. Increase in chunk_size results in more averaged angle:distance pairs but increase response time result in slower data acquisition. For faster data acquisition decrease chunk_size.<br/>
```
Note: Calibrate chunk size depends on your application and frequency of device. 
if the chunk size is not enough not all angles are covered. 
```

* `Connect` -- Begin serial connection with Lidar by opening serial port. Return success status True/False.<br />


* `StartScanning` -- Begin the lidar and returns a generator which returns a dictionary consisting angle(degrees) and distance(millimeters).<br />
 `Return Format` : {angle(0):distance, angle(2):distance,....................,angle(359):distance}<br />

* `StopScanning` -- Stops scanning but keeps serial connection alive.<br />

* `GetHealthStatus` -- Returns True if Health of lidar is good else returns False<br />

* `GetDeviceInfo` -- Returns Information of Lidar version, serial number etc.<br />

```
class FrequencyStep(Enum):
    oneTenthHertz=1
    oneHertz=2
```
* `IncreaseCurrentFrequency` -- Increase current frequency by oneTenth or one depends on enum FrequencyStep. <br/>

* `DecreaseCurrentFrequency` -- Decrease current frequency by oneTenth or one depends on enum FrequencyStep. <br/>
```
import PyLidar3
port = input("Enter port name which lidar is connected:") #windows
Obj = PyLidar3.YdLidarG4(port)
if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    print(Obj.GetCurrentFrequency())
    Obj.IncreaseCurrentFrequency(PyLidar3.FrequencyStep.oneTenthHertz)
    print(Obj.GetCurrentFrequency())
    Obj.DecreaseCurrentFrequency(PyLidar3.FrequencyStep.oneHertz)
    print(Obj.GetCurrentFrequency())
    Obj.Disconnect()
else:
    print("Error connecting to device")
```

* `EnableConstantFrequency` -- Enables constant frequency default Enable.

* `DisableConstantFrequency` -- Disable constant frequency.

* `SwitchRangingFrequency` -- Switch between ranging frequencies 4khz, 8khz and 9khz, default 9khz.

* `GetCurrentRangingFrequency` -- Returns current Ranging Frequency in khz.

* `Reset` -- Reboot the lidar <br />

* `Disconnect` -- Stop scanning and close serial communication with Lidar. <br />

## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Flakshmanmallidi%2FPyLidar3.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Flakshmanmallidi%2FPyLidar3?ref=badge_large)
