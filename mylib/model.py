"""
prediction library
"""

import random
import torch
import torch.nn.functional as f


def predict(img):
    """Returns the prediction of the image."""
    classes = ["cat", "dog", "pikachu"]
    pred = random.random()
    class_pred = int(pred * 3 % 3)
    return classes[class_pred]


def rescale(img, size):
    """Resizes the tensoflow image to a determined size."""
    if img.dim() == 3:
        img = img.unsqueeze(0)
    img_resized = f.interpolate(
        img, size=(size, size), mode="bilinear", align_corners=False
    )
    return img_resized.squeeze(0)
