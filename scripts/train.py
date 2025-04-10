from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt')  # or yolov8s.pt, etc.

    model.train(
        data='datasets/dataset/data.yaml',
        epochs=50,
        imgsz=640,
        batch=16,
        name='website-elements-detection10',
        project='results',
        device=0  # Ensure GPU usage
    )

if __name__ == '__main__':
    # Required for multiprocessing on Windows
    import multiprocessing
    multiprocessing.freeze_support()
    main()
