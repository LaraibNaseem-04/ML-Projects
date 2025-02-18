import streamlit as st
import cv2
import numpy as np
from PIL import Image

DEMO_IMAGE = 'com.png'

BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
               "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
               ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

width = 368
height = 368
inWidth = width
inHeight = height

net = cv2.dnn.readNetFromTensorflow("graph_opt.pb")

st.title("Human Pose Estimation Using OpenCV")

st.text('Make Sure you have a clear image with all the parts clearly visible')

img_file_buffer = st.file_uploader("Upload an image, Make sure you have a clear image", type=['jpeg', 'jpg', 'png'])

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))
else:
    demo_image = DEMO_IMAGE
    image = np.array(Image.open(demo_image))

# Ensure the image is in RGB format
if len(image.shape) == 2:  # Grayscale image
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
elif image.shape[2] == 4:  # RGBA image
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)

st.subheader('Original Image')
st.image(image, caption="Original Image", use_column_width=True)

thres = st.slider('Threshold for detecting the key points', min_value=0, value=20, max_value=100, step=5)

@st.cache
def PoseDetector(frame):
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    # Ensure the frame is in RGB format
    if len(frame.shape) == 2:  # Grayscale image
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
    elif frame.shape[2] == 4:  # RGBA image
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)

    net.setInput(cv2.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    out = net.forward()

    # Get performance profile
    t, _ = net.getPerfProfile()

    points = []
    for i in range(len(BODY_PARTS)):
        probMap = out[0, i, :, :]
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]

        if prob > thres / 100:
            points.append((int(x), int(y)))
        else:
            points.append(None)

    for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]

        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]

        if points[idFrom] and points[idTo]:
            cv2.line(frame, points[idFrom], points[idTo], (0, 255, 0), 2)
            cv2.circle(frame, points[idFrom], 5, (0, 0, 255), -1)
            cv2.circle(frame, points[idTo], 5, (0, 0, 255), -1)

    return frame, t

output, inference_time = PoseDetector(image)

st.subheader('Positions Estimated')
st.image(output, caption="Positions Estimated", use_column_width=True)

st.write(f"Inference time: {inference_time * 1000.0 / cv2.getTickFrequency():.2f} ms")

st.markdown('''
            ## Thank you for using Human Pose Estimation App!
            ''')