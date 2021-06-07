# JetsonNano

Visual Studio Code install
1. Downdload ARM64 .deb file from https://code.visualstudio.com/download
2. sudo apt install ./code_1.55.2-1618306574_arm64.deb

Install smbus
1. sudo apt install python3-smbus

Jetson.GPIO
https://github.com/NVIDIA/jetson-gpio
1. sudo pip install Jetson.GPIO
2. sudo groupadd -f -r gpio
3. sudo usermod -a -G gpio your_user_name
4. sudo cp lib/python/Jetson/GPIO/99-gpio.rules /etc/udev/rules.d/ or sudo cp venv/lib/pythonNN/site-packages/Jetson/GPIO/99-gpio.rules /etc/udev/rules.d/
5. sudo udevadm control --reload-rules && sudo udevadm trigger

JetsonHacks PiOLED
1. https://github.com/JetsonHacksNano/installPiOLED
2. ./installPiOLED.sh
3. cd pioled
4. python3 stats.py
5. ./createService.sh

JetsonHacks CSI-Camera
1. https://www.jetsonhacks.com/2019/04/02/jetson-nano-raspberry-pi-camera/
2. https://github.com/JetsonHacksNano/CSI-Camera
