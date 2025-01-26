import numpy as np
from skimage.transform import resize
from skimage.util import random_noise

class AllAugmentationTransform:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, video_array):
        # Example augmentation: adding random noise
        video_array = random_noise(video_array)
        return video_array

def pad(array, pad_width, mode='constant', **kwargs):
    return np.pad(array, pad_width, mode=mode, **kwargs)