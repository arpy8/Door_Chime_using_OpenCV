# Door Chime using OpenCV

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple door chime application that uses OpenCV to detect motion and trigger an audio alert.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Introduction

The "Door Chime using OpenCV" is a Python application that uses OpenCV to detect motion in a video stream and triggers an audio alert when motion is detected. This can be useful for creating a door chime or security system.

Key features of this project include:
- Real-time motion detection using OpenCV.
- Customizable audio alert when motion is detected.
- Adjustable motion threshold for sensitivity.
- Easy configuration via a JSON file.

## Prerequisites

Before using this application, make sure you have the following prerequisites installed:
- DroidCam
- Python 3
- OpenCV (cv2)
- pygame

You can install
- DroidCam using this [link](https://www.dev47apps.com/)
- OpenCV and pygame using pip:
```bash
pip install opencv-python-headless
pip install pygame
```

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/arpy8/Door_Chime_using_OpenCV.git
```

2. Change to the project directory:

```bash
cd Door_Chime_using_OpenCV
```

## Usage

To use the "Door Chime using OpenCV" application:

1. Ensure your camera is connected and configured properly.

2. Edit the `config.json` file to set the desired parameters, including the IP address of the video stream, audio file path, sleep time, and motion threshold.

3. Run the application:

```bash
python main.py
```

The application will continuously monitor the region of interest in the video stream and play the specified audio file when motion is detected.

## Configuration

The `config.json` file allows you to customize the behavior of the door chime application. You can adjust the following parameters:

- `ip`: The IP address of the video stream (e.g., droidcam_url).
- `audio_file`: Path to the audio file to be played when motion is detected.
- `sleep_time`: The duration to wait before playing the audio again (in seconds).
- `motion_threshold`: The minimum motion area required to trigger the audio alert.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.