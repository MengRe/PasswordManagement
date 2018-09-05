import argparse
import os
import pickle
import sys


def main(args):
    # 此结构用来存储数据
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
    if args.website_or_show.strip().lower() == 'show':
        account_to_show = show_all_accounts()
        print_interface(account_to_show)
    else:
        if args.option == 's':
            account_to_show = search()
            print_interface(account_to_show)
        elif args.option == 'a':
            add()
        elif args.option == 'r':
            remove()
        else:
            change()

    # 将数据写入内存
    with open(path_store, 'wb') as wf:
        pickle.dump(data_structure, wf)


def print_interface(account_to_show):
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


def show_all_accounts():
    pass


def parse_argument(argv):
    parse = argparse.ArgumentParser(description='password command line parameter')
    parse.add_argument('website_or_show', type=str,
                       help='''websit : operate this account  
                                   show: show all account in database''')
    parse.add_argument('-o', '--option', type=str, default='s', choices=['s', 'a', 'r', 'c'],
                       help=''' -o s :search  an account 
                                -o a : add an account 
                                -o r : remove an account 
                                -o c : change an account''')

    return parse.parse_args(argv)


if __name__ == '__main__':
    main(parse_argument(sys.argv[1:]))
