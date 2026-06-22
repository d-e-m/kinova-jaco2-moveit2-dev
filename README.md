# 📘 **README.md — MoveIt 2 Dev Kit for Kinova Jaco2 (ROS 2 Humble)**

## 🦾 Overview
This repository provides a **MoveIt 2 development kit** for the **Kinova Jaco2 robotic arm**, ported to **ROS 2 Humble**.  
It is designed as a practical, hands‑on starting point for developers who want to explore motion planning, kinematics, and manipulation using MoveIt 2.

The project includes:
- A full ROS 2 Humble workspace layout  
- Jaco2 URDF + meshes  
- MoveIt 2 configuration package  
- Example launch files  
- RViz2 visualization setup  
- Basic motion planning demos  

This work builds on the excellent open‑source contributions from the Kinova Robotics team and educational material from the *Learn by Doing: Manipulators* course on Udemy.

---

## 🙏 Credits

### Kinova Robotics  
URDF and mesh assets originate from the official Kinova ROS repository:  
➡️ [https://github.com/Kinovarobotics/kinova-ros](https://github.com/Kinovarobotics/kinova-ros)

### Udemy Course  
Concepts and development approach inspired by:  
➡️ *Learn by Doing: Manipulators* (Udemy)

---

## 📂 Repository Structure

```
jaco2_ws/
├── jaco2_robot_description/        # URDF, meshes, robot description
├── jaco2_robot_moveit/            # MoveIt 2 configuration package
├── jaco2_robot_control/            # Launch files and RViz configs
└── README.md
```

---

## 🚀 Installation

### 1. Create a ROS 2 Humble workspace
```bash
mkdir -p ~/jaco2_ws/src
cd ~/jaco2_ws/src
```

### 2. Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### 3. Install dependencies using rosdep
```bash
cd ~/jaco2_ws
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

### 4. Build the workspace
```bash
colcon build --symlink-install
```

### 5. Source the workspace
```bash
source install/setup.bash
```

---

## 🖥️ Running the Demo

### Launch MoveIt 2 + RViz2
```bash
ros2 launch jaco2_robot_description gazebo.launch.py
ros2 launch jaco2_robot_control controller.launch.py
ros2 launch jaco2_robot_moveit moveit.launch.py
```

This will start:
- robot_state_publisher  
- MoveIt 2  
- RViz2 with planning scene  
- Jaco2 model  

---

## 🎥 Demo Video  
```html
<video src="/media/jaco2_robot_arm_demo.mp4" controls width="600"></video>
```

```html
<video src="/media/finger_move.mp4" controls width="600"></video>
```


---

## 🛠️ Features

- **URDF-based robot description** for Jaco2  
- **MoveIt 2 configuration** with planning pipelines  
- **RViz2 visualization**  
- **Motion planning examples**  
- Ready for extension into:
  - Controllers  
  - Gazebo/Isaac simulation  
  - Custom planning pipelines  
  - Gripper integration  

---

## 📚 Learning Resources

- **Kinova ROS Documentation**  
  [https://github.com/Kinovarobotics/kinova-ros](https://github.com/Kinovarobotics/kinova-ros)

- **MoveIt 2 Tutorials**  
  [https://moveit.picknik.ai/](https://moveit.picknik.ai/)

- **ROS 2 Humble Documentation**  
  [https://docs.ros.org/en/humble/](https://docs.ros.org/en/humble/)

- **Udemy: Learn by Doing — Manipulators**  
  *(Search on Udemy for the course title)*

---

## 🤝 Contributing
Pull requests are welcome!  
If you find issues or want to add features, feel free to open an issue.

---

## 📜 License
This project follows the licensing terms of the original Kinova assets.  
Please review the Kinova repository for details.

---
