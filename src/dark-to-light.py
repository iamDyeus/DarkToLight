import os
import argparse
from PIL import Image, ImageOps

def invert_image_colors(image_path, verbose):
    """Inverts colors of an image and replaces the original file."""
    try:
        img = Image.open(image_path).convert("RGB")  # Ensure RGB mode
        inverted_img = ImageOps.invert(img)  # Invert colors
        inverted_img.save(image_path)  # Overwrite the original image
        if verbose:
            print(f"Inverted: {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_directory(directory, verbose, dry_run):
    """Recursively processes all images in the given directory and subdirectories."""
    image_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):  # Add formats if needed
                image_path = os.path.join(root, file)
                image_count += 1
                if dry_run:
                    if verbose:
                        print(f"Would invert: {image_path}")
                else:
                    invert_image_colors(image_path, verbose)
    if image_count == 0:
        print("No images found to process.")
    else:
        print(f"Total images processed: {image_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Invert colors of all images in a directory recursively.")
    parser.add_argument("directory", type=str, help="Path to the directory containing images.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without making any changes.")
    args = parser.parse_args()

    if os.path.isdir(args.directory):
        print(f"Processing directory: {args.directory}")
        process_directory(args.directory, args.verbose, args.dry_run)
        if not args.dry_run:
            print("✅ All images have been processed!")
        else:
            print("✅ Dry run completed!")
    else:
        print("❌ Error: Directory does not exist.")
