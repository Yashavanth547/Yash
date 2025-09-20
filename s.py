import streamlit as st
import cv2
import numpy as np
from pyzbar import pyzbar
import datetime
import csv
import os

LOG_FILE = "scans.csv"

# Ensure log file exists
def ensure_log_exists():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "type", "data"])

# Log scan result
def log_scan(code_type: str, data: str):
    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.datetime.now().isoformat(), code_type, data])

# Decode QR / Barcode
def decode_image(img_array):
    detections = pyzbar.decode(img_array)
    results = []
    for d in detections:
        data = d.data.decode("utf-8", errors="replace")
        type_name = d.type
        results.append((type_name, data))
    return results

# -------------------- STREAMLIT APP --------------------
st.set_page_config(page_title="📷 QR / Barcode Scanner", layout="centered")
st.title("📷 QR / Barcode Scanner")
st.write("Take a snapshot from your webcam and decode QR codes or barcodes.")

ensure_log_exists()

img_file = st.camera_input("Take a picture")

if img_file:
    # Convert uploaded image to OpenCV format
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)

    # Decode QR/barcodey

    if detections:
        st.success("✅ Detected codes:")
        for t, data in detections:
            st.write(f"**{t}** → {data}")
            log_scan(t, data)
    else:
        st.warning("⚠️ No QR / barcode detected in this frame.")

# Show previous scans
if st.checkbox("Show scan history"):
    if os.path.exists(LOG_FILE):
        st.write("### Scan History")
        st.dataframe(
            data=pd.read_csv(LOG_FILE),
            use_container_width=True
        )
    else:
        st.info("No scans yet.")
