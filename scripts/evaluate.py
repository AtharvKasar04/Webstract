from ultralytics import YOLO

def main():
    # Load trained model
    model = YOLO('results/website-elements-detection103/weights/best.pt')

    # Evaluate on the test set
    metrics = model.val(data='datasets/dataset/data.yaml', split='test')

    print("\n📊 Evaluation Results:")
    print(f"mAP@0.5:       {metrics.box.map:.4f}")
    # print(f"mAP@0.5:0.95:   {metrics.box.map50to95:.4f}")
    print(f"Precision:      {metrics.box.precision:.4f}")
    print(f"Recall:         {metrics.box.recall:.4f}")

    names = model.names
    for i, ap in enumerate(metrics.box.ap):
        print(f"→ {names[i]}: AP = {ap:.4f}")

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
