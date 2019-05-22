#
# Author Duvaragesh Kannan
#
import sys
sys.path.append("..")
from .scripts import label_image 

def namer():
    return label_image.label_image(model_file ='pages/tf_files/retrained_graph.pb' ,file_name='pages/tf_files/Signatures/Duvaragesh_Kannan/100080576_f52e8ee070_n.jpg')