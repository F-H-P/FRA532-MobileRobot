# Navigation System

### Navigate with static environment
Run Gazebo with environment:
```
ros2 launch megarover_samples_ros2 vmegarover_with_sample_world.launch.py
```
Run NAV2 package:
```
ros2 launch megarover_samples_ros2 vmegarover_navigation.launch.py
```
Run path tracking:
```
ros2 run navigation path_tracking.py
```
Run local path planner:
```
ros2 run navigation LocalPlanning_PotentialField.py
```
Run global path planner:
```
ros2 run navigation GlobalPlanning_A-star.py
```
Run behavior server:
```
ros2 run navigation Behavior_server.py
```
