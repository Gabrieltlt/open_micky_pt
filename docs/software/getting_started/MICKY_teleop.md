# 🎮 MICKY Teleop

<div style="text-align: justify;">

This section guides you through running the MICKY teleoperation.

---

## Keyboard Teleop

After installing all required packages, connect the Arduino board (already configured according to the installation guide) to your computer.

Then, open two terminals.

---

In the first terminal, run:

```bash
ros2 launch motors_controller motors_controller.launch.py
```

---

In the second terminal, run:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

---

Use the following keys to control the robot:

| Key | Action |
|-----|--------|
| `i` | Move forward |
| `,` | Move backward |
| `j` | Turn left |
| `l` | Turn right |
| `u` | Forward + left |
| `o` | Forward + right |
| `m` | Backward + left |
| `.` | Backward + right |
| `k` | Stop the robot |

---

## Joystick Teleop

It is also possible to control the robot using a Logitech game controller.

---

### Install Required Packages

```bash
sudo apt install ros-humble-joy ros-humble-teleop-twist-joy
```

---

### Connect the Controller

Connect the Logitech controller via USB or Bluetooth, and run the commands below:

To verify that it is detected:

```bash
ls /dev/input/js0
```

---

In the first terminal, run:

```bash
ros2 launch motors_controller motors_controller.launch.py
```

---

In a second terminal, run:

```bash
ros2 run joy joy_node
```

---

In a third terminal, run:

```bash
ros2 run teleop_twist_joy teleop_node
```

---

### Controls

- Left analog stick → linear motion (forward/backward and lateral)
- Right analog stick → rotation

</div>