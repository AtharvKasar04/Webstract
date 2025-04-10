from ultralytics import YOLO
import os

# Load your trained model
model = YOLO('results/website-elements-detection103/weights/best.pt')

# Folder with test images
image_dir = 'test_images'
output_dir = 'inference_results'
os.makedirs(output_dir, exist_ok=True)

# Run inference
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        path = os.path.join(image_dir, filename)
        results = model(path)

        for r in results:
            r.save(filename=os.path.join(output_dir, filename))
            r.show()  
            print(f"✅ Done: {filename}")
