# ⚙️ Locomotion System

<div style="text-align: justify;">

MICKY uses a Mecanum wheel-based locomotion system, enabling omnidirectional motion without requiring rotation of the robot body.

The system adopts a hybrid control architecture, where high-level processing is performed on a computer running **ROS 2 Humble**, while low-level control is handled by dedicated hardware. This separation ensures real-time motor actuation while maintaining flexibility for planning and decision-making.

This design is widely used in mobile robotics applications, providing improved maneuverability, scalability, and system robustness.

---

## Hardware Configuration

Motor control is managed by an **Arduino Mega 2560**, which interfaces with four **TB6600 drivers**. These drivers are responsible for actuating **Nema 23 stepper motors**.

For navigation and state estimation, the robot uses **MPU6050 sensors** connected via the I2C bus.

---

## Robot Kinematics

The robot uses **Mecanum wheels**, enabling omnidirectional motion through the combination of individual wheel velocities.

The system kinematics is based on converting the robot’s velocity commands, defined by the linear velocities in X (`v_x`) and Y (`v_y`), along with the angular velocity (`ω`), into individual wheel velocities.

This allows:

- Forward and backward motion  
- Lateral (sideways) motion  
- Rotation  
- Combined movements (e.g., diagonal motion)  

</div>