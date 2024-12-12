import cv2

# **Constants and Configuration**
OUTPUT_FILEPATH = r'C:\Users\maxim\OneDrive\Desktop\FACEID\output.mp4'
FRAME_RATE = 20.0
VIDEO_CODEC = cv2.VideoWriter_fourcc(*'mp4v')

def main():
    # **Open the default camera**
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Cannot open camera")
        return

    # **Get the default frame width and height**
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # **Define the VideoWriter object**
    out = cv2.VideoWriter(OUTPUT_FILEPATH, VIDEO_CODEC, FRAME_RATE, (frame_width, frame_height))

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Cannot receive frame")
            break

        # **Write the frame to the output file**
        out.write(frame)

        # **Display the captured frame**
        cv2.imshow('Camera', frame)

        # **Exit on 'q' key press**
        if cv2.waitKey(1) == ord('q'):
            break

    # **Release resources**
    cam.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
