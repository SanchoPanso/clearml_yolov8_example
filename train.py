from clearml import Task
from ultralytics import YOLO

# Step 1: Creating a ClearML Task
task = Task.init(project_name="my_project", task_name="my_yolov8_task")

# Step 2: Selecting the YOLO11 Model
model_variant = "yolo8n"
task.set_parameter("model_variant", model_variant)

# Step 3: Loading the YOLO11 Model
model = YOLO(f"{model_variant}.pt")

# Step 4: Setting Up Training Arguments
args = dict(data="coco8.yaml", epochs=16)
task.connect(args)

# Step 5: Initiating Model Training
results = model.train(**args)
