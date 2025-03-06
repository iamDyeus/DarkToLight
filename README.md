# DarkToLight

### Light Mode Magic for Dark Code Shots.

DarkToLight is a Python tool that transforms dark mode code screenshots into clean, light mode versions by inverting their colors. Say goodbye to straining your eyes or mismatched themes—convert your dark code outputs to bright, readable visuals with ease.

![Frame](https://github.com/user-attachments/assets/afdbb89e-f56a-4dc7-82a5-62c70e5adb66)



## Project Structure

```
DarkToLight/
├── src/              # Source code for the project
├    └── dark-to-light.py  
├
├── .gitignore        # Git ignore file for unnecessary files
├── README.md         # Project documentation (you're here!)
└── requirements.txt  # Project dependencies
```

## Features

- Converts dark mode code screenshots to light mode.
- Simple and fast image processing.
- Perfect for developers, presenters, or anyone tired of dark mode visuals.
- Perfect when you need to print output snippets.

## Requirements

- Python 3.x
- Pillow (PIL) library

## Prerequisites

- Python 3.8 or higher
- A virtual environment (recommended)

## Setup

- Clone the Repository

```bash
git clone https://github.com/iamDyeus/DarkToLight.git
cd DarkToLight
```

- Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install Dependencies

- Install the required packages:

```bash
pip install -r requirements.txt
```

(Note: Adjust dependencies based on your implementation.)

## Usage

To run the script, use the following command:

```bash
python dark-to-light.py input_image_path output_image_path
```

Replace `input_image_path` with the path to the dark image you want to convert and `output_image_path` with the path where you want to save the converted image.

## Example
#### Single Image Conversion:
```bash
python dark-to-light.py images/dark_image.jpg images/light_image.jpg
```

This command will take `dark_image.jpg` from the `images` directory and save the converted light image as `light_image.jpg` in the same directory.


#### Batch Image Conversion:
```bash
python dark-to-light.py your_directory
```

This command will convert all the images in the specified directory to light mode.


## License

This project is licensed under the MIT License.

