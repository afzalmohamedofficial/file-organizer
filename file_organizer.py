import os
import shutil

user_input = "./"

target_folder_images = os.path.join(user_input, "Images")
target_folder_videos = os.path.join(user_input, "Videos")
target_folder_documents = os.path.join(user_input, "Documents")
other_folder = os.path.join(user_input, "Others")
    

for folder in [target_folder_images, target_folder_videos, target_folder_documents, other_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)


for filename in os.listdir(user_input):
    source_path = os.path.join(user_input, filename)
    if os.path.isfile(source_path): 
        if filename.lower().endswith((".jpeg", ".jpg", ".png", ".gif")):
            try:
                shutil.move(source_path, target_folder_images)
            except Exception as e:
                print(f"Error moving {filename}: {e}")
         
        elif filename.lower().endswith((".mp4", ".mkv", ".mov")):
            try:
                shutil.move(source_path, target_folder_videos)
            except Exception as e:
                print(f"Error moving {filename}: {e}")
                    
        elif filename.lower().endswith((".pdf", ".docx", ".txt")):
            try:
                shutil.move(source_path, target_folder_documents)
            except Exception as e:
                print(f"Error moving {filename}: {e}")
             
        else:
            try:
                shutil.move(source_path, other_folder)
            except Exception as e:
                print(f"Error moving {filename}: {e}")
                
            

print("Done organizing your files!")






    



    
    



        
        
