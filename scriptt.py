import exifread

def process_img(path):
    f = open(path, 'rb')
    tags = exifread.process_file(f)
    info = {
        'Image DateTime': tags.get('Image DateTime', '0'),
        'GPS GPSLatitudeRef': tags.get('GPS GPSLatitudeRef', '0'),
        'GPS GPSLatitude': tags.get('GPS GPSLatitude', '0'),
        'GPS GPSLongitudeRef': tags.get('GPS GPSLongitudeRef', '0'),
        'GPS GPSLongitude': tags.get('GPS GPSLongitude', '0')
    }
    return info

info = process_img('filename')
print(info)

