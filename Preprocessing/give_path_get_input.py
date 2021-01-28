def func(path):
  import os
  import nibabel as nib
  import matplotlib.pyplot as plt
  import numpy as np
  import cv2

  path_time_step0 = path + '/0.nii.gz'
  path_time_step6 = path + '/6.nii.gz'

  time_step0 = nib.load(path_time_step0)
  time_step6 = nib.load(path_time_step6)

  ts0 = time_step0.get_fdata()
  ts6 = time_step6.get_fdata()

  ts0 = np.reshape(ts0,(1,256,256,64,1))
  ts6 = np.reshape(ts6,(1,256,256,64,1))

  y = [ts0,ts6]

  return y
