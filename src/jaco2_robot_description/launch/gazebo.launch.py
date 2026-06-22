import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    jaco2_robot_description_dir = get_package_share_directory("jaco2_robot_description")

    model_arg = DeclareLaunchArgument(name="model", default_value=os.path.join(
                                        jaco2_robot_description_dir, "urdf", "jaco2_robot.xacro"
                                        ),
                                      description="Absolute path to robot urdf file")
    
    ros_distro = os.environ["ROS_DISTRO"]
    is_ignition = "True" if ros_distro == "humble" else "False"
    robot_description = ParameterValue(Command(["xacro ",
                                    LaunchConfiguration("model"),
                                    " is_ignition:=",
                                    is_ignition
                                    ]),
                                    value_type=str)
    
    gazebo_resource_path = SetEnvironmentVariable(
        name="GZ_SIM_RESOURCE_PATH",
        value=[str(Path(jaco2_robot_description_dir).parent.resolve())]
    )
    
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description,
                     "use_sim_time": True}]
    )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )
    
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory("ros_gz_sim"),
                "launch"
            ),
            "/gz_sim.launch.py"
        ]),
        launch_arguments=[
            ("gz_args", [" -v 4 -r empty.sdf"])
        ]
    )
    
    gz_sapwm_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
            "-topic", "robot_description",
            "-name", "jaco2_robot"
        ]
    )
    
    gz_sapwm_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
            "-topic", "robot_description",
            "-name", "jaco2_robot",
            # Set your initial joint positions here using -J <joint_name> <value>
            # You will need to change 'joint_1', 'joint_2' to match your actual URDF joint names
            # and adjust the radians (e.g., 3.14, 1.57) to achieve your exact "upward" pose.
            # "-J", "jaco2_robot_joint_1", "0.0", 
            # "-J", "jaco2_robot_joint_2", "-3.14159", 
            # "-J", "jaco2_robot_joint_3", "-3.14159",
            # "-allow_renaming", "true"
        ]
    )
    
    gz_ros2_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock"
        ]
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", os.path.join(jaco2_robot_description_dir, "rviz", "alligning.rviz")],
    )

    return LaunchDescription([
        model_arg,
        gazebo_resource_path,
        robot_state_publisher_node,
        # joint_state_publisher_gui_node,
        gazebo,
        gz_sapwm_entity,
        gz_ros2_bridge,
        # rviz_node
    ])