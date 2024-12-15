import os
import requests
import json
import csv

# Base URL and Pagination Configuration
BASE_API_URL = "https://www.ajio.com/api/category/830309004?fields=SITE&currentPage={page}&pageSize=45&format=json"
OUTPUT_DIR = "images_product"
CSV_FILE = "images_product/product_details.csv"
ERROR_LOG_FILE = "images_product/image_download_failures.log"

# Ensure the output directory for images exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Function to download a single image
def download_image(image_url, image_name):
    try:
        response = requests.get(image_url, stream=True, timeout=10)
        if response.status_code == 200:
            image_path = os.path.join(OUTPUT_DIR, image_name)
            with open(image_path, 'wb') as img_file:
                for chunk in response.iter_content(1024):
                    img_file.write(chunk)
            return image_path
        else:
            raise Exception(f"HTTP {response.status_code}")
    except Exception as e:
        with open(ERROR_LOG_FILE, "a") as log_file:
            log_file.write(f"Failed to download {image_url} - Error: {e}\n")
        return None

# Function to fetch and save product details
def fetch_and_save_products():
    page = 1
    all_products = []

    # Open CSV File for Writing
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["Product Code", "Product Name", "Brand", "Category", "Offer Price", "Original Price", 
                      "Discount Percent", "Product URL", "Image Path", "Image Status"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Pagination Loop
        while True:
            print(f"Fetching page {page}...")
            try:
                response = requests.get(BASE_API_URL.format(page=page), timeout=10)
                if response.status_code != 200:
                    print("Failed to fetch data.")
                    break

                data = response.json()
                products = data.get("products", [])

                # If no products are returned, stop pagination
                if not products:
                    print("No more products found.")
                    break

                for product in products:
                    # Extract required product details
                    product_code = product.get("code")
                    product_name = product.get("name")
                    brand_name = product.get("fnlColorVariantData", {}).get("brandName")
                    category = product.get("brickName")
                    offer_price = product.get("offerPrice")
                    original_price = product.get("wasPriceData", {}).get("value")
                    discount_percent = product.get("discountPercent")
                    product_url = "https://www.ajio.com" + product.get("url", "")

                    # Skip products missing required details
                    if not (product_code and product_name and offer_price and product_url and product.get("images")):
                        print(f"Skipping incomplete product: {product_name}")
                        continue

                    # Download the first image
                    first_image_url = product.get("images")[0].get("url")
                    unique_image_name = f"{product_code}_{product_name.replace(' ', '_')}.jpg"
                    image_path = download_image(first_image_url, unique_image_name)

                    # Determine image status
                    image_status = "Success" if image_path else "Failed"

                    # Write product details to CSV
                    writer.writerow({
                        "Product Code": product_code,
                        "Product Name": product_name,
                        "Brand": brand_name,
                        "Category": category,
                        "Offer Price": offer_price,
                        "Original Price": original_price,
                        "Discount Percent": discount_percent,
                        "Product URL": product_url,
                        "Image Path": image_path or "N/A",
                        "Image Status": image_status
                    })

                    # Append product details for JSON saving
                    all_products.append({
                        "Product Code": product_code,
                        "Product Name": product_name,
                        "Brand": brand_name,
                        "Category": category,
                        "Offer Price": offer_price,
                        "Original Price": original_price,
                        "Discount Percent": discount_percent,
                        "Product URL": product_url,
                        "Image Path": image_path or "N/A",
                        "Image Status": image_status
                    })

                # Move to the next page
                page += 1

            except Exception as e:
                print(f"Error on page {page}: {e}")
                break

    # Save all products to JSON for reference
    with open("product_details.json", "w", encoding="utf-8") as json_file:
        json.dump(all_products, json_file, indent=4)
    print("Data saved successfully to CSV and JSON.")
    print(f"Failed image logs saved in {ERROR_LOG_FILE}")

# Main Execution
if __name__ == "__main__":
    fetch_and_save_products()
