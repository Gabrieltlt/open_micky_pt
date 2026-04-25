# 🧪 MICKY Simulation

<div style="text-align: justify;">

This section guides you through running the MICKY simulation environment using Gazebo and ROS 2.

---

## Step 1 — Launch Gazebo

1. Opens Gazebo Harmonic with the `turtlebot3_world` world and spawns the Micky robot.

```bash
ros2 launch micky_simulation gazebo.launch.py
```

Wait until Gazebo GUI is fully open and the robot model is visible in the scene.

---

## Step 2 — Launch SLAM

2. In a **new terminal**, start the SLAM node and RViz:

```bash
ros2 launch micky_slam sim_slam.launch.py
```

RViz will open with the `/map` topic displayed. The map starts empty and is built as the robot moves.

---

## Step 3 — Drive the Robot (Teleop)

3. In a **third terminal**, start the keyboard teleop:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

| Key | Action |
|---|---|
| `i` / `,` | Forward / backward |
| `j` / `l` | Strafe left / right |
| `u` / `o` | Rotate left / right |
| `space` | Stop |
| `w` / `x` | Increase / decrease linear speed |

Drive the robot around the entire environment. The map in RViz fills in as new areas are scanned. For best results, make at least one full loop so slam_toolbox can close the loop.

---

4. The robot can be vizualized and controled with teleop, like the image below: 

<div align="center">
<video width="60%" controls>
  <source src="../../_static/videos/simulation.mp4" type="video/mp4">
</video>
</div>

## Step 4 — Save the Map

Once the environment is fully mapped, run in any terminal:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/micky_map
```

This generates two files:
- `~/your_map.pgm` — the occupancy grid image
- `~/your_map.yaml` — metadata (resolution, origin, thresholds)

---

## Common Troubleshooting

### Gazebo does not open / freezes on startup

```bash
pkill -f gz_sim && pkill -f gzserver
unset IGN_PARTITION GZ_PARTITION
```

Then re-run Step 1.

### Map stays empty in RViz

1. Check that the LiDAR is publishing:
   ```bash
   ros2 topic echo /laser_scan_front
   # Expected: ~10 Hz
   ```
2. Move the robot — slam_toolbox only registers a new scan after the robot travels at least **0.5 m**.

### Robot does not move

```bash
# Test the command manually
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist \
  "{linear: {x: 0.2, y: 0.0, z: 0.0}, angular: {z: 0.0}}" --once
```

If the robot moves in Gazebo but not from teleop, make sure the teleop terminal has focus (keyboard input is captured there).

</div>