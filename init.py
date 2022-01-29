import os
from unicodedata import name
from flask import Flask,render_template
from HMprep import HM_matrix
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time

app = Flask(__name__,template_folder='templates')

def save_fig(image,heatmap_matrix,new_plot_name,num):
    x , y = 1 , 1
    plt.subplot(1,x,y)
    plt.axis('off')
    plt.imshow(image)
    plt.imshow(heatmap_matrix/255, alpha=0.3, cmap='seismic')
    plt.tight_layout(w_pad=-10)
    if num==1:
            name_f = 'IMG1_1249_s_heat'
    else :
            name_f = 'IMG2_1249_s_heat'
    for filename in os.listdir('E:\SSS\SeniorPy\Flask\static'):
        if name_f in filename:
            os.remove('E:\SSS\SeniorPy\Flask\static\\'+filename)
    plt.savefig('E:\SSS\SeniorPy\Flask\static\\'+new_plot_name,format='jpg',bbox_inches='tight',
                    pad_inches = 0)

@app.route('/')
def display_img():
    image1 , heatmap_matrix1 = HM_matrix('IMG_1249_s.jpg',gaussian_std=2)
    new_plot_name_1 = 'IMG1_1249_s_heat'+str(time.time())+'.jpg'
    save_fig(image1,heatmap_matrix1,new_plot_name_1,1)
    image2 , heatmap_matrix2 = HM_matrix('IMG_1249_s.jpg',gaussian_std=2)
    new_plot_name_2 = 'IMG2_1249_s_heat'+str(time.time())+'.jpg'
    save_fig(image2,heatmap_matrix2,new_plot_name_2,2)
    return render_template('index.html',graph1=new_plot_name_1,graph2=new_plot_name_2)


@app.route('/home')
def Hello():
    return 'Hello World'
