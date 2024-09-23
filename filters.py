from PIL import Image, ImageFilter, ImageOps

def apply_filter(input_path, output_path, filter_type):
    img = Image.open(input_path)
    
    if filter_type == 'grayscale':
        img = ImageOps.grayscale(img)
    elif filter_type == 'blur':
        img = img.filter(ImageFilter.BLUR)
    elif filter_type == 'contour':
        img = img.filter(ImageFilter.CONTOUR)
    elif filter_type == 'detail':
        img = img.filter(ImageFilter.DETAIL)
    elif filter_type == 'sharpen':
        img = img.filter(ImageFilter.SHARPEN)
    else:
        raise ValueError("Unknown filter type")
    
    img.save(output_path)
