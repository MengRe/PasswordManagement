import os
import pickle


def main():
    # 用来存储数据
    data_structure = []
    dir_to_store = os.path.dirname(__file__)
    relative_path = 'dataSave.pickle'
    path_store = os.path.join(dir_to_store, relative_path)

    if not os.path.exists(path_store):
        print('没有创建文件，我们就创一个了')
        # 创建文件
        with open(path_store, 'wb') as wf:
            pickle.dump(list(), wf)
    # 将数据加载到内存中
    with open(path_store, 'rb') as rf:
        data_structure = pickle.load(rf)

    # 正常写程序

    # 将数据写入内存
    with open(path_store, 'wb') as wf:
        pickle.dump(data_structure, wf)


def print_interface():
    # firstly, write these code
    # need parameter to identify the number of characters:  a dict of collections.default,  default is 30
    pass


def add():
    # 添加之前需要判断是否已经存在，若存在  元祖的前三个完全相同， 则不添加
    pass


def change():
    pass


def search():
    pass


def remove():
    pass
