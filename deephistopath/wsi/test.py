from slide import open_slide, show_slide, slide_info, slide_stats

if __name__ == "__main__":
    # s = open_slide('/mnt/960EVO/workspace/python-wsi-preprocessing/deephistopath/11b6a83d-c94c-44eb-a3b3-aa6d086ad2bc')
    # show_slide(1)
    s = open_slide('/media/disk2/TUPAC16/training_image_data/TUPAC-TR-017.svs')
    print(type(s))
    slide_stats()
    pass
