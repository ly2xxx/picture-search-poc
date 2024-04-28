import streamlit as st
import os
from pathlib import Path
from sentence_transformers import SentenceTransformer
# import weaviate
# from weaviate.classes.config import Property, DataType
# import libraries
import streamlit as st
import tkinter as tk
from tkinter import filedialog

# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
st.title("Add Images to Weaviate")
st.write('Please select a folder:')
clicked = st.button('Folder Picker')
if clicked:
    st.session_state["image_path"] = st.text_input('Selected folder:', filedialog.askdirectory(master=root))
else:
    st.stop()

# # Initialize SentenceTransformer model
# model = SentenceTransformer('clip-ViT-B-32')

# # Connect to the local Weaviate instance
# client = weaviate.connect_to_local()

# # Clean up existing collection (if any)
# COLLECTION_NAME = "MyImagesLocal"
# client.collections.delete(COLLECTION_NAME)

# # Create a new collection with 'name' and 'path' properties
# client.collections.create(
#     COLLECTION_NAME,
#     properties=[
#         Property(name="name", data_type=DataType.TEXT),
#         Property(name="path", data_type=DataType.TEXT),
#     ]
# )

# # Get the collection
# images_collection = client.collections.get(COLLECTION_NAME)

# # Input: Image folder path
# img_folder = st.session_state["image_path"]#st.sidebar.text_input("Image folder path:")

# # Button to add images
# # if st.button("Add images under "+img_folder):
# img_files = Path(img_folder).glob("*")
# # Total number of images
# num_images = len(list(Path(img_folder).glob("*"))) 
# # Progress bar
# progress_bar = st.progress(0)

# with images_collection.batch.dynamic() as batch:
#     i=0
#     for img_path in img_files:
#         # Calculate progress  
#         i += 1
#         progress = int(100 * (i) / num_images)
#         progress_bar.progress(progress)
#         try:
#             # Process image
#             img_name = os.path.basename(img_path)
#             img_emb = model.encode(str(img_path))

#             # Add the image object to Weaviate
#             batch.add_object(properties={
#                 "name": img_name,
#                 "path": str(img_path)
#             }, vector=img_emb.tolist())
#         except Exception as e:
#             print(f"Error processing {img_path}: {e}")

# st.success("Images added to Weaviate!")

# # Close progress bar when done
# progress_bar.empty()

# # Close the Weaviate client
# client.close()
