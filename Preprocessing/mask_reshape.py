def mask_reshape(path):
  import os
  import nibabel as nib
  import matplotlib.pyplot as plt
  import numpy as np
  import cv2
  # load_mask = nib.load(path)
  load_mask = path
  reshape_mask = np.reshape(load_mask,(1, 256, 256, 64, 1))

  return reshape_mask
