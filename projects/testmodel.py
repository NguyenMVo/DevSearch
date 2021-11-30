import tensorflow as tf 
from tensorflow import keras
import os
import matplotlib as plt 
from PIL import Image
import numpy as np

file_path = r'C:\Toan\Deep learning\web\product\images\Camera.jpg'
model_test = keras.models.load_model(os.path.join('projects', './model', 'xception_model.h5'))
list_class = {15:'QuanAo',17:'TuiVi',2:'Camera',10:'MayGiat',21:'XeTai',19:'XeDapDien',16:'TuLanh',0:'Amply',4:'DienThoai',13:'NuocHoa',6:'GiayDep',11:'MayLanh',12:'MayTinhBang',18:'XeDap',7:'GiuongNem',14:'Oto',20:'XeMay',5:'DongHo',9:'Laptop',3:'CayCanh',1:'BanGhe',8:'KeTu'}

def test(file_path):
    
    
    # text = model_test.predict()
    img = Image.open(file_path)
    img = img.resize((224,224))
    img = img.convert("RGB")
    img = np.expand_dims(img, axis=0)
    img = img.reshape(224,224,3)
    
    text = model_test.predict(np.expand_dims(img/255.0,0))[0]
    text = np.argmax(text)
    print(list_class[text])
    return text
    
# for r in os.listdir(r'C:\Toan\Deep learning\web\product\images\\'):
#     print(r)
#     test(os.path.join(r'C:\Toan\Deep learning\web\product\images', r))
# test(file_path)