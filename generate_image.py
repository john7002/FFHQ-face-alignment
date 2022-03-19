import argparse
from numpy.core.numeric import True_
from tqdm import tqdm
import os
from landmarks import get_face_landmarks
from ffhq_align import recreate_aligned_images


AVAILABLE_METHODS = ['mediapipe','dlib']

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("-i","--InFolder", help="directory to image(s)",required=True)
    a.add_argument("-o","--OutFolder", help="path to generated images",required=True)
    a.add_argument("-m","--method", help="Select face landmark method, default is mediapipe")
    a.add_argument("-p","--padding",help="Use padding. Default is True",type=bool,default = True)
    a.add_argument("-r","--rotate_level",help="Rotate face. default is True",type=bool,default=True)
    a.add_argument("-s","--size_output",help="image output size, default is 1024",type=int)

    args = a.parse_args()
    
    input_folder= args.InFolder
    output_folder= args.OutFolder
    output_size = args.size_output
    rotate_level = args.rotate_level
    padding = args.padding
    if output_size <=0:
        print("output_size must be at least 128px")
        exit(0)
    if args.method:
        method = args.method
        if method in AVAILABLE_METHODS:
            print(f"Will align images using {args.method}")
        else:
            print("Unknown method, only 'dlib' or 'mediapipe' available")
            exit(0)
    else:
        method = 'mediapipe'
        print(f"Will align images using mediapipe")


    included_extensions = ['jpg','jpeg', 'bmp', 'png']   
    file_names = [fn for fn in sorted(os.listdir(input_folder)) if any(fn.endswith(ext) for ext in included_extensions)]   

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with tqdm(total = len(file_names)) as pbar:
        for pic_name in file_names:
            pic_path = os.path.join(input_folder,pic_name)
            pic_root = pic_name.split('.')[0] #align images have same name as original
            faces_detected = get_face_landmarks(pic_path,method=method)


            for i, face_landmarks in enumerate(faces_detected):
                if len(faces_detected)>1:
                    face_img_name = f"{pic_root}_{i}.png"
                else:
                    face_img_name = f"{pic_root}.png" 
                image = recreate_aligned_images(pic_path, os.path.join(output_folder, face_img_name),face_landmarks,method=method,rotate_level=rotate_level,output_size=output_size,enable_padding=padding)
            pbar.update()

