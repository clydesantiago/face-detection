import cv2
from deepface import DeepFace
import threading
import queue

def analyze_frame(q, result, lock):
    while True:
        frame = q.get()
        if frame is None:
            break
        try:
            analysis = DeepFace.analyze(
                frame,
                actions=['age', 'gender'],
                enforce_detection=False,
                detector_backend='retinaface'  # You can try 'ssd' for faster processing
            )
            if isinstance(analysis, list):
                analysis = analysis[0]
            age = analysis['age']
            gender_info = analysis['gender']
            
            if isinstance(gender_info, dict):
                gender = max(gender_info, key=gender_info.get)
            else:
                gender = 'Unknown'

            if gender == 'Man':
                display_gender = 'Male'
            elif gender == 'Woman':
                display_gender = 'Female'
            else:
                display_gender = 'Unknown'

            # Extract face region
            if 'region' in analysis:
                region = analysis['region']
                x, y, w, h = region['x'], region['y'], region['w'], region['h']
                face_box = (x, y, w, h)
            else:
                face_box = None

            with lock:
                result['age'] = age
                result['gender'] = display_gender
                result['face_box'] = face_box
                # Debug: Print updated age, gender, and face box
                print(f"Updated Result -> Age: {age}, Gender: {display_gender}, Face Box: {face_box}")
        except Exception as e:
            print(f"Analysis error: {e}")
            with lock:
                # Set age and gender to indicate no face was detected
                result['age'] = 'No face detected'
                result['gender'] = 'No face detected'
                result['face_box'] = None

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    q = queue.Queue(maxsize=1)  # Limit queue size to 1
    result = {'age': 'N/A', 'gender': 'Unknown', 'face_box': None}
    lock = threading.Lock()

    # Start analysis thread
    thread = threading.Thread(target=analyze_frame, args=(q, result, lock))
    thread.start()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Ensure only the latest frame is in the queue
        if not q.full():
            q.put(frame_rgb)
        else:
            try:
                # Remove the oldest frame
                q.get_nowait()
                q.put_nowait(frame_rgb)
            except queue.Full:
                pass  # If queue is still full, skip this frame

        # Safely access the result
        with lock:
            age = result.get('age', 'N/A')
            gender = result.get('gender', 'Unknown')
            face_box = result.get('face_box', None)

        # Display age and gender
        cv2.putText(frame, f"Age: {age}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, f"Gender: {gender}", (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Draw green box around detected face
        if face_box:
            x, y, w, h = face_box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Age and Gender Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stop the analysis thread
    q.put(None)
    thread.join()

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
