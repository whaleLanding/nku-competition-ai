from flask import Flask,render_template,request
import io
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获得前端传过来的图片对象
        file = request.files['file']
        # 获取图片对象的名字（包含后缀）
        file_name_extension = file.filename
        # 获取图片对象的名字（不包含后缀）
        file_name, _ = (file_name_extension.rsplit('.', 1))
        # 获取当前python文件的绝对路径
        current_file_path = os.path.abspath(__file__)
        # 获取给定文件所在的文件夹路径
        current_folder_path = os.path.dirname(current_file_path)
        # 生成保存文件的文件夹路径
        save_dir = current_folder_path+r'\static\images'
        # 生成保存文件的路径
        file_save_path = os.path.join(save_dir, file_name_extension)
        # 将指定文件保存在文件保存路径
        file.save(file_save_path)
        return render_template('display.html',image_name = file_name)
    else:
        return render_template('index.html')  


if __name__ == '__main__':
    app.run()