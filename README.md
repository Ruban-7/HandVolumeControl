# Hand Gesture Volume Control

This project demonstrates a real-time hand gesture recognition system that allows users to control the system volume using hand gestures. Built with Python, OpenCV, Mediapipe, and Pycaw, it highlights the application of computer vision in creating intuitive user interfaces.

## Features

- **Real-time Hand Tracking**: Detects and tracks hand landmarks accurately.
- **Dynamic Volume Control**: Maps the distance between the thumb and index finger to system volume levels.
- **Smooth and Interactive UI**: Provides visual feedback for detected gestures and volume changes.

## Technologies Used

- **Programming Language**: Python
- **Libraries**: OpenCV, Mediapipe, Pycaw, NumPy
- **Concepts**: Computer Vision, Hand Gesture Recognition, Real-time Processing

## How It Works

1. The program uses the Mediapipe library to detect and track hand landmarks in real time.
2. The distance between the thumb and index finger is calculated using the detected landmarks.
3. The system volume is adjusted based on this distance, with smooth transitions for better user experience.
4. Live feedback, such as volume percentage and gesture status, is displayed on the screen.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/YourUsername/HandVolumeControl.git
    ```

2. Install required dependencies:

    ```bash
    pip install opencv-python mediapipe pycaw comtypes numpy
    ```

3. Run the program:

    ```bash
    python VolumeHandControlAdvance.py
    ```

**Explanation**: YouTube link will be updated soon.

Feel free to replace `YourUsername` with your actual GitHub username in the repository URL.
