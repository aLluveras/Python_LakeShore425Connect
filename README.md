# Python_LakeShore425Connect
Connecting to a LakeShore425 Gaussmeter via Python

To allow user access to the LakeShore 425 Gaussmeter in Linux, create the file: /etc/udev/rules.d/52-lakeshore425.rules, with contents:
```
SUBSYSTEMS=="usb",ATTRS{idVendor}=="1fb9",ATTRS{idProduct}=="0401",MODE="0666",SYMLINK+="lakeshore425"
```
Then reload the udev rules with:
```
sudo udevadm control --reload-rules
sudo udevadm trigger
```

The device will be accessible through /dev/lakeshore425

Dependencies:
-Pymeasure
-PyVisa
-pyqtgraph
 
Important: In visa.py might be necessary to change "import visa" for "import pyvisa"
