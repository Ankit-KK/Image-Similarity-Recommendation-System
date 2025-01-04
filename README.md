# Image Similarity Recommendation System

## Overview
This project implements an **Image Similarity Recommendation System** that identifies and recommends visually similar product images. The system supports metadata cleaning, image scraping, and similarity calculations for recommendations.

## Features
- **Metadata Cleaning**: Handles missing or inconsistent image metadata.
- **Image Scraping**: Scrapes images from online sources.
  - **Without Metadata**: `Image_scrapping.py`
  - **With Metadata**: `imageWithMetadata.py`
- **Recommendation System**: Uses a Python program to compute image similarity.
  - **Recommendation File**: `recommend.py`

## Technologies Used
- Python
- Requests
- -Json
- TensorFlow & Keras
- NumPy, SciPy
- Matplotlib
- Pandas

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ankit-KK/Image-Similarity-Recommendation-System.git
   cd Image-Similarity-Recommendation-System
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Prepare your image dataset and metadata files under appropriate directories.

## Usage
### 1. Cleaning Metadata
Run the script to clean metadata of images:
```bash
python CleaningCSVforMissingImages.py
```

### 2. Image Scraping
- To scrape images **only**:
   ```bash
   python Image_scrapping.py
   ```
- To scrape images **with metadata**:
   ```bash
   python imageWithMetadata.py
   ```

### 3. Recommendation System
To compute image similarity and generate recommendations:
```bash
python recommend.py
```

## File Structure
- `CleaningCSVforMissingImages.py`: Cleans metadata and handles missing images.
- `Image_scrapping.py`: Scrapes images without metadata.
- `imageWithMetadata.py`: Scrapes images along with metadata.
- `recommend.py`: Computes image similarity and recommends images.
- `requirements.txt`: Dependency list.
- `product_images/`: Directory for input images.

  

## Acknowledgements
- VGG16 pre-trained model (ImageNet)
- TensorFlow/Keras
- BeautifulSoup for web scraping

## Author
[Ankit-KK](https://github.com/Ankit-KK)
