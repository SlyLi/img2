import os


def read_dictory(path):
    for f_name in os.listdir(path):
        print('![](https://slyli.cn/img2/fav-sfw/%s)'%f_name)


if __name__ == "__main__":
    path = './fav-sfw1'
    read_dictory(path)