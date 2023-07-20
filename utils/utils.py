import uuid
import os
from django.core.exceptions import ValidationError

def generate_unique_filename(instance, filename, field_name):
    # Get the file's extension
    ext = filename.split('.')[-1]
    # Generate a unique filename
    unique_filename = f"{uuid.uuid4()}.{ext}"
    # Return the unique filename 

    return os.path.join(instance.upload_directory, field_name, unique_filename)

def generate_cover_photo_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'cover_photo')

def generate_pitch_video_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'pitch_video')

def generate_unsigned_nda_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'unsigned_nda')

def generate_pitch_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'pitch')

def generate_signed_nda_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'signed_nda')

def generate_signed_ncnd_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'signed_ncnd')

def generate_identity_proof_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'identity_proof')

def generate_profile_picture_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'profile_picture')

def generate_avtar_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'avtar')

def generate_company_proof_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'company_proof')

def generate_profile_photo_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'profile_photo')

def generate_organisation_document_filename(instance, filename):
    return generate_unique_filename(instance, filename, 'organisation_document')


def validate_100_word_limit(value):
    word_limit = 100  # Set the desired word limit
    words = value.split()
    if len(words) > word_limit:
        raise ValidationError(f"Exceeded the maximum word limit of {word_limit} words.")
    
def validate_1000_word_limit(value):
    word_limit = 1000  # Set the desired word limit
    words = value.split()
    if len(words) > word_limit:
        raise ValidationError(f"Exceeded the maximum word limit of {word_limit} words.")
    
def validate_200_word_limit(value):
    word_limit = 200  # Set the desired word limit
    words = value.split()
    if len(words) > word_limit:
        raise ValidationError(f"Exceeded the maximum word limit of {word_limit} words.")
    
def validate_150_word_limit(value):
    word_limit = 150  # Set the desired word limit
    words = value.split()
    if len(words) > word_limit:
        raise ValidationError(f"Exceeded the maximum word limit of {word_limit} words.")