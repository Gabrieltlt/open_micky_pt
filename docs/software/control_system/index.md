# 🧠 Control System

<div style="text-align: justify;">

The MICKY control system follows a hybrid architecture, combining high-level processing with low-level embedded control.

This section presents the locomotion control system of MICKY.

---

## Communication

Communication between the onboard computer and the microcontroller is performed via a serial interface.

Velocity commands are transmitted using the following format:

```text
<v_x, v_y, ω>
```

This lightweight protocol ensures low-latency communication between high-level and low-level systems.

---

## Microcontroller Firmware

The microcontroller firmware is designed for low-latency and non-blocking execution.

It uses the `Wire.h` and `AccelStepper.h` libraries to ensure efficient motor control and sensor communication.

The main control loop consists of:

1. Serial command reception  
2. Safety mechanism (fail-safe)  
3. Kinematic processing  
4. Sensor acquisition  
5. Motor control  

Telemetry includes:

- orientation  
- acceleration  
- angular velocity  
- temperature  

---

## ROS 2 Integration

The system is integrated with ROS 2 through two main nodes:

- **CmdVelToSerial** — converts velocity commands into serial messages  
- **ImuSerialPublisher** — publishes IMU data  

This architecture allows seamless integration with higher-level navigation and control frameworks.

</div>