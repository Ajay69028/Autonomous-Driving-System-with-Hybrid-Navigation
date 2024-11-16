The presentation titled *"Autonomous Driving with Hybrid System"* outlines a project conducted by a group of students guided by Mr. Ravi Teja, affiliated with the Department of Electrical and Electronics Engineering at Koneru Lakshmaiah Education Foundation. The project integrates real-time obstacle detection and voice-controlled navigation using the Model Predictive Control (MPC) algorithm to ensure efficient and safe navigation. Here is a detailed explanation of its sections:

Literature Review and Objectives:
The project seeks to balance automation with user control, enhancing both safety and ease of use in navigation systems. It utilizes ultrasonic sensors for obstacle detection and a microphone for voice commands. The MPC algorithm processes these inputs, enabling precise execution and adaptive driving. The primary objectives include:
- Real-time obstacle detection using ultrasonic sensors.
- Seamless voice control for navigation through a microphone.
- Integration of MPC for accurate and effective navigation.

Components and Technologies:
The project employs a variety of hardware:
- *Raspberry Pi Pico:* Acts as the processing unit.
- *L298N Motor Driver, Ultrasonic Sensors, and DC Motors:* Enable mobility and obstacle detection.
- *Microphone and Buzzer:* Facilitate voice control and alerts.
- *HWB Batteries:* Provide power to the system.

System Architecture and Control Mechanism:
The system operates through a sequence of monitoring and execution:
1. Obstacle Detected: The drive motor slows, and the user provides directional input. The system calculates the required wheel rotation angle, and a servo motor adjusts the vehicle’s path.
2. No Obstacle Detected: The vehicle continues moving while sensors remain active to anticipate changes in the environment.

The use of ultrasonic sensors ensures accurate obstacle detection and effective system alignment.

Why Model Predictive Control (MPC):
The MPC algorithm is pivotal in making the navigation system efficient and user-friendly. It calculates optimal steering angles based on speed, proximity to obstacles, and environmental factors. Unlike traditional methods that result in abrupt movements, MPC enables controlled and gradual turns, enhancing the system’s maneuverability and safety.

Advantages:
The system offers several benefits:
- Hands-free navigation via intuitive voice commands.
- Smooth and calculated turns through MPC, avoiding abrupt maneuvers.
- Dynamic adaptation to environmental changes for efficient navigation.
- Real-time responsiveness due to TOF (Time of Flight) sensors.

Applications:
The technology has potential applications in:
- Voice-Controlled Home Assistants: Navigating around furniture efficiently.
- Home Delivery Bots: Safely delivering items using voice-guided movements.
- Cleaning Robots: Operating in specific rooms based on user commands.

Conclusion and References:
The project demonstrates a hybrid system blending safety, efficiency, and flexibility in navigation systems. The team has also referenced significant studies and works on MPC to substantiate their methodology, including research on vehicle trajectory tracking and robust MPC frameworks.

The presentation concludes with a brief demonstration plan and citations of scholarly articles, emphasizing the theoretical foundation of their approach.
