# ⬇️ Install MICKY

<div style="text-align: justify;">

To install MICKY, follow the commands below.

---

## Requirements

Make sure you have the following installed:

* Ubuntu 22.04
* ROS 2 Humble
* Arduino IDE or PlatformIO
* Gazebo Harmonic (or Garden)

---

## Install MICKY Base Controller

Clone the repository:

```bash
mkdir -p /micky_ws/src && cd micky_ws/src
git clone https://github.com/FBOTWork/micky_base_controller.git
cd micky_base_controller
```

---

## Firmware Setup

Upload the firmware to the Arduino Mega:

1. Open the firmware file:

```bash
firmware_micro_controller/firmware.ino
```

2. Connect the Arduino

3. Configure in Arduino IDE:

* Board: **Arduino Mega 2560**
* Port: `/dev/ttyACM0` or `/dev/ttyUSB0`

4. Click **Upload**

---

## USB Configuration (udev)

Configure a persistent device name for the Arduino.

### Get device information

```bash
udevadm info -a -n /dev/ttyACM0 | grep -E 'idVendor|idProduct|serial'
```

### Create udev rule

```bash
sudo nano /etc/udev/rules.d/99-arduino_robo.rules
```

Add:

```bash
SUBSYSTEM=="tty", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="0043", MODE="0666", SYMLINK+="arduino_robo"
```

### Reload rules

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

### Verify device

```bash
ls /dev/arduino_robo
```

### (Optional) Add user permissions

```bash
sudo usermod -aG dialout $USER
```

Log out and log back in after running this command.

---

## Install MICKY Simulation

Navigate to your workspace source directory and clone the repository:

```bash
cd ~/micky_ws/src
git clone https://github.com/FBOTWork/micky_simulation.git
```

Install rosdep dependencies:

```bash
cd ~/micky_ws
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

Install required ROS 2 packages:

```bash
sudo apt install -y \
  ros-humble-ros-gz-sim \
  ros-humble-ros-gz-bridge \
  ros-humble-robot-state-publisher \
  ros-humble-slam-toolbox \
  ros-humble-nav2-map-server \
  ros-humble-xacro \
  ros-humble-rviz2
```

---

## Building the Workspace

Run **once** after cloning or modifying package files:

```bash
cd ~/micky_ws
colcon build --symlink-install
source install/setup.bash
```

</div>