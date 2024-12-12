import cv2
import imagehash
from PIL import Image
import time

def compare_images(cv2_img, comparison_img_path, cutoff=5):
    # Convert cv2 image from OpenCV format to PIL format
    pil_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(pil_img)  # Explicit conversion to PIL Image

    # Load the comparison image using PIL
    comparison_img = Image.open(comparison_img_path)

    # Get the average hashes of both images
    hash0 = imagehash.average_hash(pil_img)
    hash1 = imagehash.average_hash(comparison_img)

    # Calculate the hash difference
    hash_diff = hash0 - hash1

    # Check if the images are similar
    is_similar = hash_diff < cutoff
    if is_similar:
        print("These images are similar!")
    return is_similar

def main():
    # **Live Camera Setup**
    cam = cv2.VideoCapture(0)  # Use default camera (index 0)
    if not cam.isOpened():
        print("Cannot open camera")
        return

    # **Reference Image Path**
    comparison_img_path = 'C:\\Users\\maxim\\OneDrive\\Desktop\\FACEID\\MAX.jpg'

    max_retries = 3
    retry_delay = 2  # seconds
    settings = True

    while settings == True:
        # **Capture Frame from Live Camera**
        ret, cv2_img = cam.read()
        if not ret:
            print("Cannot receive frame")
            break

        # **Display Live Camera Feed**
        cv2.imshow('Live Camera', cv2_img)

        # **Compare Captured Frame to Reference Image with Retry**
        retries = 0
        similar = compare_images(cv2_img, comparison_img_path, cutoff=10)
        print(f"Images similar: {similar}")
        if similar == False:
            while retries < max_retries: # Overwrite previous output
                print("Retrying...")
                time.sleep(retry_delay)
                retries += 1
        else:
            settings = False

        # **Exit on 'q' Key Press**
        if cv2.waitKey(1) == ord('q'):
            break

    # **Release Resources**
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
