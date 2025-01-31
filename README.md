# EditPhoto: IMAGE PROCESSING USING PILLOW LIBRARY

EditPhoto is an advanced yet user-friendly image processing web application built with Flask and Pillow (PIL). It allows users to upload images from their computer storage and apply various image transformations and filters seamlessly.

---

## 🚀 Features

🔹 **Upload & Process Images:** Users can upload images and apply various transformations.

🔹 **Image Editing Functions:**
- **Rotate**: Rotate images by 90 degrees with each click.
- **Crop**: Select an area using the cursor and crop accordingly.
- **Blur**: Apply a blurring effect for a soft look.
- **Contrast Adjustment**: Increase or decrease contrast levels.
- **Filters:** Sharpen, Smooth, Edge Enhance, Emboss, Grayscale, and Sepia.

🔹 **Interactive UI/UX:**
- Dynamic navigation bar that adapts to scrolling.
- Smooth animations for an elegant experience.
- Intuitive image editor at the core of EditPhoto.
- Stylish custom buttons and visually appealing clip backgrounds.

---

## 🛠 Algorithmic Analysis

### 🔐 Secret Key Handling
Secure session cookies are managed using a `secret_key` to maintain user sessions across different routes in Flask.

### 📂 Image Upload Mechanism
Flask is configured to save uploaded images in an `uploads` directory:
```python
app.config['UPLOAD_FOLDER'] = 'uploads'
```
This ensures that images are accessible for processing when required.

### 🖼 Image Processing
A dedicated function, `process_image()`, applies various transformations:
```python
image.rotate(angle)  # Rotate image by 90 degrees per click
image.crop(x1, y1, x2, y2)  # Crop image using user-specified coordinates
image.filter(ImageFilter.<filter_property>)  # Apply filters (Blur, Sharpen, etc.)
image.convert('L')  # Convert image to grayscale
enhancer.enhance(con*variable)  # Adjust contrast levels
```

### 🔀 Routing System
- **First Route:** Uploads the image, processes it, and stores the path in a session key.
- **`/apply_filter` Route:** Calls `process_image()` to apply the selected transformation and encodes the result in Base64 for display on the webpage.
- **Other Routes (`/about`, `/team`)** provide information about the developers.

---

## 💡 Novel Features

✔️ **JavaScript-Powered Cropping:** Enables users to select crop areas dynamically.
✔️ **Session-Based Image Handling:** Uses Flask sessions to temporarily store and process images.
✔️ **Hidden Button Functionality:** Buttons are initially hidden and only appear when interacting with the parent button.
✔️ **Canvas Utilization:** HTML `<canvas>` is used for graphical manipulations and rendering images dynamically.

---

## 🎨 Frontend UI/UX Highlights

✨ **Dynamic Navigation Bar:** Transparent on load, turns white on scroll.
✨ **Creative Backgrounds:** Stunning visuals with dark overlays and text.
✨ **Smooth Animations:** Engaging user experience with scrolling animations.
✨ **Custom Buttons:** Stylish play buttons for enhanced interactivity.
✨ **Clip Backgrounds:** Aesthetically pleasing clipped backgrounds.
✨ **Fully Responsive Layout:** Designed for a seamless experience on all devices.
✨ **Well-Designed Footer:** Quick access to essential links and information.

---

## 🎯 How to Run the Project

1️⃣ Clone the repository:
```sh
git clone https://github.com/saurabhjnv93/saurabhMayankdhp_2024_2.git
```

2️⃣ Navigate to the project directory:
```sh
cd EditPhoto
```

3️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

4️⃣ Run the Flask server:
```sh
python app.py
```

5️⃣ Open your browser and visit:
```sh
http://127.0.0.1:5000/
```
---

🚀 **Visit EditPhoto today and unleash your creativity!** 🎨

