import os
from matplotlib.pyplot import imshow

import deephistopath.wsi.slide as slide

def file_stats(file_dir, file_name):
    """
    Print Stats from openslide and py-wsi. Show scaled image at the end.
    
    Args:
        file_dir: The directory containing wsi files.
        file_name: The wsi file name.
    """    
    # info 1
    print('Openslide info:\n')
    slide.single_slide_info(os.path.join(file_dir, file_name))
    print('\n\n\n')
    # show image
    pil_img , large_h, large_w, new_h, new_w = slide.show_scaled_slide_image(os.path.join(file_dir, file_name))
    imshow(pil_img)