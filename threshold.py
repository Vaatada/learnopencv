import cv2
import numpy as np
import os

def convert_to_average_rgb_threshold(image_path, output_dir, threshold_value):
    try:
        img = cv2.imread(image_path)
        if img is None:
            print(f"无法读取图片：{image_path}")
            return None, None

        height, width, channels = img.shape
        # 创建一个与原图相同大小的新图片，用于存储均值结果
        avg_img = np.zeros_like(img)
        
        # 创建一个与原图相同大小的新图片，用于存储阈值处理结果
        threshold_img = np.zeros_like(img)

        # 计算每个像素的RGB平均值
        average_values = np.mean(img, axis=2, keepdims=True)

        # 将平均值赋给所有通道
        avg_img = np.repeat(average_values, 3, axis=2).astype(np.uint8)

        # 手动实现阈值处理
        mask = (average_values > threshold_value)
        # 大于阈值的设为255，否则为0
        threshold_result = np.where(mask, 255, 0).astype(np.uint8)
        threshold_img = np.repeat(threshold_result, 3, axis=2)

        os.makedirs(output_dir, exist_ok=True)

        # 构建输出文件路径
        base_filename = os.path.basename(image_path).split('.')[0]
        avg_output = os.path.join(output_dir, f"{base_filename}_avg.jpg")
        threshold_output = os.path.join(output_dir, f"{base_filename}_threshold_{threshold_value}.jpg")

        # 保存均值图像和阈值处理后的图像
        cv2.imwrite(avg_output, avg_img)
        print(f"均值图像已保存到: {avg_output}")
        
        cv2.imwrite(threshold_output, threshold_img)
        print(f"阈值{threshold_value}处理后的图像已保存到: {threshold_output}")
        
        return avg_img, threshold_img
    except Exception as e:
        print(f"处理图像时出错: {e}")
        return None, None

# 测试不同阈值
def test_different_thresholds(image_path, output_dir, threshold_values):
    for threshold in threshold_values:
        print(f"处理阈值:{threshold}")
        convert_to_average_rgb_threshold(image_path, output_dir, threshold)

# 使用os.path.join确保路径格式正确
input_image = os.path.join('C:', 'Users', 'Lenovo', 'Desktop', 'image', 'img2.jpg')
output_dir = os.path.join('C:', 'Users', 'Lenovo', 'Desktop', 'image')

# 多个阈值测试
thresholds = [50, 100, 150, 200]  # 不同的阈值值
test_different_thresholds(input_image, output_dir, thresholds)