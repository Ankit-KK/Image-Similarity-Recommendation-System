import os
import csv

# Input and Output file paths
CSV_FILE = "images_product/product_details.csv"  # Input CSV file
CLEANED_CSV_FILE = "images_product/cleaned_product_details.csv"  # Output cleaned CSV file
IMAGE_DIR = "images_product/"  # Directory containing images

def validate_images_and_clean_csv():
    valid_rows = []

    # Open the CSV file to read
    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames  # Preserve the original column headers

        # Process each row
        for row in reader:
            image_path = row.get("Image Path", "").strip()
            image_status = row.get("Image Status", "Failed")  # Optional fallback

            if image_status == "Success" and image_path:  # Check only successful image rows
                # Check if the image file exists
                if os.path.isfile(image_path):
                    valid_rows.append(row)  # Keep this row as image exists
                else:
                    print(f"Image not found: {image_path}. Removing row.")
            else:
                print(f"Skipping row with failed image status: {row.get('Product Name')}")

    # Write valid rows to a new CSV file
    with open(CLEANED_CSV_FILE, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()  # Write column headers
        writer.writerows(valid_rows)  # Write valid rows

    print(f"Cleaned CSV file saved as: {CLEANED_CSV_FILE}")

if __name__ == "__main__":
    validate_images_and_clean_csv()
