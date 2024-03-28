def detect_objects(image_path):
    related_path = image_path

    from ultralytics import YOLO
    import cv2
    import supervision as sv
    import json

    model = YOLO('yolov8m-world.pt')

    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    cap = cv2.VideoCapture(related_path)  # Here's should be a path !
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

    out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))

    cleaned = list()

    while cap.isOpened():
        ret, img = cap.read()

        if not ret:
            break

        results = model.predict(img)
        detections = sv.Detections.from_ultralytics(results[0])

        index = list()
        names_dictionary = model.names.copy()

        for i in detections.class_id:
            index.append(i)

        cleaned = [names_dictionary[key] for key in index]
        cleaned = ['#' + tag for tag in cleaned]
        cleaned = ', '.join(list(set(cleaned)))
        print(cleaned)  # For debug

    out.release()
    cap.release()
    cv2.destroyAllWindows()

    return cleaned


if __name__ == "__main__":
    path = '../../static/uploads/photos/f09afbff-e85e-4ece-8704-899f8dbb9086_ww.jpg'
    result = detect_objects(path)

    another_list = list(result)
