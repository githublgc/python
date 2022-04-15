import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
#自定义傅里叶变换功能函数
def dft(img):
    #获取图像属性
    H,W,channel=img.shape
    #定义频域图，从公式可以看出为求出结果为复数，因此，需要定义为复数矩阵
    F = np.zeros((H, W,channel), dtype=np.complex)
    # 准备与原始图像位置相对应的处理索引
    x = np.tile(np.arange(W), (H, 1))
    y = np.arange(H).repeat(W).reshape(H, -1)
    #通过公式遍历
    for c in range(channel):#对彩色的3通道数进行遍历
        for u in range(H):
            for v in range(W):
                F[u, v, c] = np.sum(img[..., c] * np.exp(-2j * np.pi * (x * u / W + y * v / H))) / np.sqrt(H * W)
    return F
#读取图像
img=cv2.imread("1.jpg")
#进行图像裁剪，加快傅里叶运算速率。将原始尺寸缩放为100*100的尺寸
img = cv2.resize(img, (100, 100), interpolation=cv2.INTER_CUBIC)
#BGR转换为RGB显示格式，方便通过matplotlib进行图像显示
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#调用傅里叶变换函数
result =dft(img)
#将傅里叶频谱图从左上角移动到中心位置
fshift = np.fft.fftshift(result)
#将复数转为浮点数进行傅里叶频谱图显示
fimg = np.log(np.abs(fshift))
#图像显示
plt.subplot(121), plt.imshow(img), plt.title('原图像')
plt.axis('off')
plt.subplot(122), plt.imshow(fimg), plt.title('傅里叶变换')
plt.axis('off')
plt.show()
