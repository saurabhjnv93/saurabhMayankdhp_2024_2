            image.save(buffered, format="PNG")
            img_data = base64.b64encode(buffered.getvalue()).decode()
    return render_template('index.html', img_data=img_data)