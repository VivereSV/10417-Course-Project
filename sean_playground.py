import torch
import torchvision as tv
import torch.functional as F
import torch.nn.functional
import torchvision.datasets as dset
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
import pycocotools
from pycocotools.coco import COCO
import matplotlib.pyplot as plt
import PIL
import skimage.io as io

from util import CenterCropTensor, TransformAnn, transformCoCoPairs

annFile = 'COCO_DATASET/annotations/instances_val2017.json'
coco=COCO(annFile)

filter_classes = "person"

# coco_val = dset.CocoDetection(root='COCO_DATASET/val2017',
#                         annFile='COCO_DATASET/annotations/instances_val2017.json',
#                         transform=transforms.ToTensor())

catIds = coco.getCatIds(catNms=filter_classes)
imgIds = coco.getImgIds(catIds=catIds)
print("Number of images containing all the classes:", len(imgIds))