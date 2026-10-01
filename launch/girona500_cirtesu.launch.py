from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    # Buscamos la ruta de stonefish_ros2 dinámicamente
    stonefish_simulator_launch = PathJoinSubstitution([
        FindPackageShare('stonefish_ros2'),
        'launch',
        'stonefish_simulator.launch.py'
    ])

    simulator_action = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(stonefish_simulator_launch),
        launch_arguments={
            'simulation_data': PathJoinSubstitution([
                FindPackageShare('girona500_stonefish'), 'data'
            ]),
            'scenario_desc': PathJoinSubstitution([
                FindPackageShare('girona500_stonefish'), 'scenarios', 'girona500_cirtesu_arucos.scn'
            ]),
            'simulation_rate': '50.0',
            'window_res_x': '1200',
            'window_res_y': '800',
            'rendering_quality': 'high',
            'sensors_sim_leak_topic': '/girona500/stonefish/sensors/leak',
            'sensors_sim_set_leak_service': '/girona500/stonefish/sensors/set_leak',
            'sensors_sim_battery_topic': '/girona500/stonefish/sensors/battery',
            'sensors_sim_battery_parameter_service': '/battery_status_simulated/set_parameters'
        }.items()
    )

    description_action = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            FindPackageShare('girona500_description'),
            'launch',
            'robot_description.launch.py'
        ]))
    )

    dvl_converter_action = Node(
        package='girona500_stonefish',
        executable='dvl_to_twist_node',
        name='dvl_to_twist_node',
        output='screen',
        parameters=[{
            'input_topic': '/girona500/navigator/dvl',
            'output_topic': '/girona500/stonefish/sensors/dvl'
        }]
    )

    battery_status_action = Node(
        package='girona500_stonefish',
        executable='battery_status_simulated',
        name='battery_status_simulated',
        output='screen',
        parameters=[{
            'battery_topic': '/girona500/stonefish/sensors/battery',
            'thruster_topics': ['/girona500/controller/thruster_setpoints_sim'],
            'battery_frame_id': 'girona500/battery'
        }]
    )

    leak_sensors_action = Node(
        package='girona500_stonefish',
        executable='leak_sensors_simulated',
        name='leak_sensors_simulated',
        output='screen',
        parameters=[{
            'leak_topic': '/girona500/stonefish/sensors/leak',
            'set_leak_service': '/girona500/stonefish/sensors/set_leak',
            'sensor_frames': ['girona500/Vehicle'],
            'leak_detected': [False]
        }]
    )

    return LaunchDescription([
        simulator_action,
        description_action,
        dvl_converter_action,
        battery_status_action,
        leak_sensors_action
    ])
