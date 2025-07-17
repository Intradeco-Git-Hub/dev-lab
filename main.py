import functions_framework

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def main(cloud_event):
    """Triggered by a change in a storage bucket."""
    data = cloud_event.data
    bucket_name = data['bucket']
    file_name = data['name']
    
    print(f"Processing file: {file_name} from bucket: {bucket_name}")
    
    # Here you can add your logic to process the file
    # For example, reading the file, transforming it, etc.
    
    print("File processing completed.")