import torch
import torch.nn as nn
from mmdet.models import HEADS
from mmcv.runner import BaseModule

@HEADS.register_module()
class SimpleOccHead(BaseModule):


    def __init__(self, )