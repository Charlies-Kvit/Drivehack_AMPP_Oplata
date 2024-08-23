from flask import Flask, Response
import cv2

app = Flask(__name__)

def capture_image():
    # Open the webcam (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Could not open webcam")

    # Capture a single frame
    ret, frame = cap.read()

    # Release the webcam
    cap.release()

    if not ret:
        raise RuntimeError("Failed to capture image from webcam")

    # Encode the frame as JPEG
    ret, jpeg = cv2.imencode('.jpg', frame)

    if not ret:
        raise RuntimeError("Failed to encode image to JPEG")

    # Convert to bytes and return
    return jpeg.tobytes()

@app.route('/capture', methods=['GET'])
def capture():
    try:
        # Capture the image from the webcam
        image = capture_image()

        # Send the image as a response with the correct MIME type
        return Response(image, mimetype='image/jpeg')

    except RuntimeError as e:
        return str(e), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5001)
