import os

def save_uploaded_file(uploaded_file):
    """
    Save uploaded file to local storage
    """
    folder = "uploads"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path
