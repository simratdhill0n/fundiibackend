import uuid
import os

def generate_unique_filename(instance, filename, field_name):
    # Get the file's extension
    ext = filename.split('.')[-1]
    # Generate a unique filename
    unique_filename = f"{uuid.uuid4()}.{ext}"
    # Return the unique filename 

    return os.path.join(instance.upload_directory, field_name, unique_filename)