# Image Similarity Recommendation System

## Overview
The **Image Similarity Recommendation System** uses deep learning techniques to recommend visually similar product images based on a query image. The system utilizes a pre-trained VGG16 model for feature extraction and cosine similarity to rank and suggest the most similar images from a dataset of product images.

## Features
- **Feature Extraction**: Leverages VGG16 model pre-trained on ImageNet to extract image features.
- **Cosine Similarity**: Measures the similarity between images using cosine distance between feature vectors.
- **Image Preprocessing**: Resizes and normalizes images for model compatibility.
- **Visualization**: Displays the input image and the top recommended images based on similarity.

## Technologies Used
- Python
- TensorFlow & Keras
- VGG16 Pre-trained Model
- Matplotlib for visualization
- NumPy & SciPy for data processing

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ankit-kk/image-similarity-recommender.git
cd image-similarity-recommender
```

### 2. Install Required Libraries
You can install the necessary libraries using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Prepare the Data
Ensure that your product images are stored in the `/content/product_images/product_images/` directory (or update the directory path in the code). The images should be in `.jpg` format for compatibility with the system.

### 4. Running the System
To run the recommendation system, execute the following in your terminal:
```bash
python recommend.py
```

You can change the input image by modifying the `input_image_path` in the script.

## File Structure
```
/image-similarity-recommender
│
├── /product_images/           # Folder containing the product images
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Acknowledgements
- VGG16 model pre-trained on ImageNet
- TensorFlow & Keras for deep learning frameworks

