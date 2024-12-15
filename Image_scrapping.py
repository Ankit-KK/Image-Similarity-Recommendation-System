import os
import requests
import json

# Function to fetch JSON data for a given page
def fetch_page_data(page):
    api_url = f"https://www.ajio.com/api/category/830309004?fields=SITE&currentPage={page}&pageSize=45&format=json&query=%3Arelevance&sortBy=relevance&gridColumns=3&advfilter=true&platform=Desktop&showAdsOnNextPage=true&is_ads_enable_plp=true&displayRatings="
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise error for HTTP issues
        return response.json()
    except Exception as e:
        print(f"Error fetching page {page}: {e}")
        return None

# Function to get the first image URL for a product
def get_product_image(product):
    try:
        # Priority 1: First image from 'images'
        if "images" in product and product["images"]:
            return product["images"][0]["url"]

        # Priority 2: First image from 'extraImages'
        if "extraImages" in product and product["extraImages"]:
            for extra in product["extraImages"]:
                if "images" in extra and extra["images"]:
                    return extra["images"][0]["url"]

        # Default: No image found
        return None
    except Exception as e:
        print(f"Error fetching image for product: {e}")
        return None

# Function to download and save an image
def download_image(image_url, product_name):
    try:
        if not image_url:
            print(f"No image URL for product: {product_name}")
            return
        
        # Format filename (sanitize product name)
        filename = f"{product_name.replace(' ', '_').replace('/', '_')}.jpg"
        file_path = os.path.join("product_images", filename)
        
        # Download the image
        response = requests.get(image_url)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        
        
    except Exception as e:
        print(f"Error downloading image {image_url}: {e}")

# Main function to handle pagination and download images
def main():
    os.makedirs("product_images", exist_ok=True)  # Create folder for images
    total_pages = 238  # Set the number of pages to scrape (can be increased)
    
    for page in range(1, total_pages + 1):
        print(f"Fetching page {page}...")
        data = fetch_page_data(page)
        
        if not data or "products" not in data:
            print(f"No products found on page {page}")
            continue
        
        # Process each product
        for product in data["products"]:
            try:
                product_name = product.get("name", "Unknown_Product")
                image_url = get_product_image(product)
                
                if image_url:
                    download_image(image_url, product_name)
                else:
                    print(f"No image found for product: {product_name}")
            except Exception as e:
                print(f"Error processing product: {e}")

if __name__ == "__main__":
    main()