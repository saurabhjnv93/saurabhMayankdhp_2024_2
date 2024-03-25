from flask import Flask, render_template, request, session
from PIL import Image, ImageFilter, ImageEnhance
from io import BytesIO
import base64
import os

app = Flask(__name__)
# This section to save the uploaded image to access when we apply filters
app.secret_key = 'abcdef'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Funtion which contains all the filters using pillow library..
def process_image(image, operation, crop_coords=None):
    if operation == 'rotate':
        image = image.rotate(90)
    elif operation == 'crop' and crop_coords:
        x1, y1, x2, y2 = map(int, crop_coords)
        image = image.crop((x1, y1, x2, y2))
    elif operation == 'blur':
        image = image.filter(ImageFilter.BLUR)
    elif operation == 'increase_contrast':
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.5)
        session['contrast_level'] = 1.5
    elif operation == 'decrease_contrast':
        current_contrast = session.get('contrast_level', 1.0)
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(current_contrast * 0.8)
        session['contrast_level'] = current_contrast * 0.8
    elif operation == 'sharpen':
        image = image.filter(ImageFilter.SHARPEN)
    elif operation == 'smooth':
        image = image.filter(ImageFilter.SMOOTH)
    elif operation == 'edge_enhance':
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif operation == 'emboss':
        image = image.filter(ImageFilter.EMBOSS)
    elif operation == 'grayscale':
        image = image.convert('L')  # Convert to grayscale
    elif operation == 'sepia':
        sepia_filter = ImageEnhance.Color(image.convert('L'))
        image = sepia_filter.enhance(0.9)  # Adjust the factor as needed for sepia tone
    return image

# This route take image from the user and convert that into accesible form.
@app.route('/', methods=['GET', 'POST'])
def front():
    img_data = None
    placeholder_image = '../static/static/placeholder.png'  # Provide the path to your placeholder image
    if request.method == 'POST':
        uploaded_file = request.files['image']
        if uploaded_file:
            image = Image.open(BytesIO(uploaded_file.read()))
            temp_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_image.png')
            image.save(temp_file_path, format="PNG")
            session['temp_file_path'] = temp_file_path
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_data = base64.b64encode(buffered.getvalue()).decode()
    return render_template('index.html', img_data=img_data)
# This is for about section 
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
# This will give brief intro of developers
@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('Team.html')

# This route is main part her we called procces_image
# funtion with various parameter 
# to do specific filter on the selected image
@app.route('/apply_filter', methods=['POST'])
def apply_filter():
    img_data = None
    selected_filter = request.form['Operation']
    temp_file_path = session.get('temp_file_path')
    if temp_file_path:
        processed_image = Image.open(temp_file_path)
        if selected_filter == 'crop':
            x1 = request.form['x1']
            y1 = request.form['y1']
            x2 = request.form['x2']
            y2 = request.form['y2']
            if x1 and y1 and x2 and y2:
                crop_coords = (int(x1), int(y1), int(x2), int(y2))
            else:
                crop_coords = None
        else:
            crop_coords = None
        processed_image = process_image(processed_image, selected_filter, crop_coords)
        processed_image.save(temp_file_path, format="PNG")
        buffered = BytesIO()
        processed_image.save(buffered, format="PNG")
        img_data = base64.b64encode(buffered.getvalue()).decode()
    return render_template('index.html', img_data=img_data)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True,port=8000)