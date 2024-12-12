# Age and Gender Detection

A real-time application that detects and displays the age and gender of individuals using your webcam. The application utilizes OpenCV for video capture and display, DeepFace for facial analysis, and threading to ensure a smooth and responsive user experience. Additionally, it visually highlights detected faces with green bounding boxes.

## Features

- **Real-Time Age and Gender Detection:** Analyzes live webcam feed to estimate the age and gender of detected faces.
- **Face Bounding Box:** Draws a green rectangle around detected faces for visual feedback.
- **No Face Detection Alert:** Displays "No face detected" when no faces are present in the frame.
- **Smooth Preview:** Utilizes threading and queue management to maintain a high frame rate and responsive display.

## Requirements

- **Python Version:** Python 3.7 or higher

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/age-gender-detection.git
   cd age-gender-detection
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   Ensure you have `pip` installed. Then, install the required Python packages using the provided `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

   **`requirements.txt` Contents:**

   ```plaintext
   opencv-python
    numpy>=1.24.3
    deepface
    tensorflow>=2.13.0
    retina-face>=0.0.13
   ```

## Usage

Run the main Python script to start the application:

```bash
python main.py
```

### Controls

- **Exit Application:** Press the `q` key to quit the application.

### What to Expect

- Upon running, a window titled "Age and Gender Detection" will appear, displaying the live webcam feed.
- When a face is detected:
  - A green box will outline the face.
  - Estimated age and gender will be displayed on the screen.
- If no face is detected:
  - The application will display "No face detected" for both age and gender.

## Troubleshooting

- **Webcam Not Detected:**

  - Ensure your webcam is properly connected and not being used by another application.
  - Verify that OpenCV is correctly installed.

- **Performance Issues:**

  - If the preview is laggy, consider lowering the webcam resolution or switching the detector backend to `'ssd'` for faster processing by modifying the `detector_backend` parameter in `main.py`.

- **DeepFace Errors:**
  - Ensure all dependencies, especially TensorFlow, are correctly installed and compatible with your Python version.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [DeepFace](https://github.com/serengil/deepface) for providing the facial analysis library.
- [OpenCV](https://opencv.org/) for computer vision functionalities.
- [TensorFlow](https://www.tensorflow.org/) for machine learning backend support.
- [RetinaFace](https://github.com/serengil/deepface/tree/master/deepface/commons/models) for accurate face detection.

---

_Feel free to customize this README to better fit your project's specifics and repository structure._
