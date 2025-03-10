import cv2
import numpy as np

def convert_to_average_rgb(image_path, output_path):
    img=cv2.imread(image_path)
    if img is None:
        print(f"无法读取图片：{image_path}")
        return

    height,width,channels=img.shape
    # 创建一个与原图相同大小的新图片
    result=np.zeros_like(img)
    # 计算每个像素的RGB平均值
    average_values=np.mean(img,axis=2,keepdims=True)
    # 将平均值赋给所有通道
    result=np.repeat(average_values,3,axis=2).astype(np.uint8)

    cv2.imwrite(output_path,result)
    print(f"处理后的图片已保存到: {output_path}")

    return result

input_image = 'C:\\Users\Lenovo\Desktop\image\img2.jpg'  # 输入图片路径
output_image = 'C:\\Users\Lenovo\Desktop\image\img2_average_rgb.jpg'  # 输出图片路径
convert_to_average_rgb(input_image, output_image)