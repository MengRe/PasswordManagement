import argparse
import os
import pickle
import sys


# (website, nickname,password, email, phone)
def main(args):
    # 此结构用来存储数据
    data_structure = {'account_saved': [], 'account_deleted': []}

    dir_to_store = os.path.dirname(__file__)
    relative_path = 'dataSave.pickle'
    path_store = os.path.join(dir_to_store, relative_path)

    if not os.path.exists(path_store):
        print('没有创建文件，我们就创一个了')
        # 创建文件
        with open(path_store, 'wb') as wf:
            pickle.dump(data_structure, wf)
    # 将数据加载到内存中
    with open(path_store, 'rb') as rf:
        data = pickle.load(rf)
        data_saved = data['account_saved']
        data_deleted = data['account_deleted']
        print('数据库中的账号：', data_saved)
        print('从数据库中删除的账号：', data_deleted)
        # print(type(data_structure))

        password_management = passwordManagement(data_saved)
    # get_max_chr(data_saved)


    # 正常写程序
    if args.website_or_show.strip().lower() == 'show':
        account_to_show = password_management.show_all_accounts()
        print_interface(account_to_show)
    else:
        if args.option == 's':
            account_to_show = password_management.search(args.website_or_show)
            print_interface(account_to_show)
        elif args.option == 'a':
            data_saved = password_management.add(args.website_or_show)
        elif args.option == 'r':
            (code, returned_data) = password_management.remove(args.website_or_show)
            if code == 0:
                data_saved = returned_data[1]
                data_deleted = returned_data[0]
            else:
                data_saved = returned_data


        else:
            data_saved = password_management.change(args.website_or_show)

    # 将数据写入内存
    with open(path_store, 'wb') as wf:
        data_structure['account_saved'] = data_saved
        data_structure['account_deleted'] = data_deleted
        pickle.dump(data_structure, wf)


def print_interface(code_and_information):
    # firstly, write these code
    # need parameter to identify the number of characters:  a dict of collections.default,  default is 30
    code, information = code_and_information
    if code == 0:
        print(information)
    elif code == 1:
        _print_information(information)


    else:
        # print(information[0], information[1])
        print('原账户信息：')
        _print_information([information[0]])
        print('修改后账户信息：')
        _print_information([information[1]])


def _print_information(information):
    dict_to_reserve_characters = get_max_chr(information)
    num_web = dict_to_reserve_characters['char_web']
    num_nick = dict_to_reserve_characters['char_nickname']
    num_passw = dict_to_reserve_characters['char_passw']
    num_email = dict_to_reserve_characters['char_email']
    num_phone = dict_to_reserve_characters['char_phone']
    print('*' * 140)
    print('|number{}|website{}|nickname{}|password{}|email{}|phonenumber{}|'.format(
        ' ' * (7 - 6), ' ' * (num_web - 7),
        ' ' * (num_nick - 8), ' ' * (num_passw - 8),
        ' ' * (num_email - 5), ' ' * (num_phone - 11)))
    for num, item in enumerate(information):
        print('|{}{}|{}{}|{}{}|{}{}|{}{}|{}{}|'.format(
            num, ' ' * (7 - len(str(num))),
            item[0], ' ' * (num_web - len(item[0])),
            item[1], ' ' * (num_nick - len(item[1])),
            item[2], ' ' * (num_passw - len(item[2])),
            item[3], ' ' * (num_email - len(item[3])),
            item[4], ' ' * (num_phone - len(item[4]))
        ))


def get_max_chr(data_saved):
    dict_to_reserve_characters = {'char_web': 10, 'char_nickname': 15, 'char_passw': 20,
                                  'char_email': 30, 'char_phone': 12}
    if data_saved:
        # 取出
        website_char, nickname_char, passw_char, email_char, phone_char = zip(*data_saved)
        max_num_char_website = len(sorted(website_char, key=lambda web: len(web), reverse=True)[0])
        max_num_char_nickname = len(sorted(nickname_char, key=lambda nickname: len(nickname), reverse=True)[0])
        max_num_char_email = len(sorted(email_char, key=lambda email: len(email), reverse=True)[0])
        max_num_char_passw = len(sorted(passw_char, key=lambda passw: len(passw), reverse=True)[0])

        if max_num_char_website > dict_to_reserve_characters['char_web']:
            dict_to_reserve_characters['char_web'] = max_num_char_website
        if max_num_char_nickname > dict_to_reserve_characters['char_nickname']:
            dict_to_reserve_characters['char_nickname'] = max_num_char_nickname
        if max_num_char_email > dict_to_reserve_characters['char_email']:
            dict_to_reserve_characters['char_email'] = max_num_char_email
        if max_num_char_passw > dict_to_reserve_characters['char_passw']:
            dict_to_reserve_characters['char_passw'] = max_num_char_passw

        return dict_to_reserve_characters


class passwordManagement(object):
    def __init__(self, data_saved, **kwargs):
        self.__data_saved = data_saved
        super().__init__(**kwargs)

    def _add_account(self, add_website):
        add_nickname = input('请输入网站昵称(输入结束后请按‘Enter‘键)：')
        add_passw = input("请输入密码：")
        add_email = input("请输入注册邮箱(若无直接按‘Enter’键):")
        add_phone = input('请输入注册手机(若无直接按‘Enter’键):')
        account = (add_website, add_nickname, add_passw, add_email, add_phone)
        self.__data_saved.append(account)
        print('您向数据库添加的网站账户为：')
        print_interface((1, account))

    def add(self, add_website):
        # print('我要添加账号')

        # 添加之前需要判断是否已经存在，若存在  元祖的前三个完全相同， 则不添加

        items = []
        for item in self.__data_saved:
            if add_website.strip().lower() == item[0].strip().lower():
                items.append(item)
        # print(items)
        if items:
            print('数据库已有相同网站的账户')
            print_interface((1, items))
            add_or_no = input('是否继续注册(继续输入y,退出输入n)若输入指令错误则默认退出：')
            if add_or_no in ['y', 'Y']:
                self._add_account(add_website)
            else:
                print('未向数据库添加网站账号，退出程序')
        else:
            self._add_account(add_website)

        return self.__data_saved

    def change(self, website):
        items = []
        for item in self.__data_saved:
            if website.strip().lower() in item[0].strip().lower():
                items.append(item)
        if not items:
            print_interface((0, '数据库中没有此网站的注册账号咩'))
        else:
            be_to_remove = {str(num): account for num, account in enumerate(items)}
            print('在数据库中搜索到的网站：')
            print_interface((1, items))
            max_num = len(items)
            remove_or_no = input('是否还要修改账号,(继续输入y,退出输入n)若输入指令错误则默认不修改:')
            if remove_or_no in ['y', 'Y']:
                number_to_be_removed = input('请输入要修改的网站账号数字0~{}:'.format(max_num - 1))
                while int(number_to_be_removed.strip()) > max_num:
                    number_to_be_removed = input('输入数字超出{}, 请重新输入：'.format(max_num))
                print('输入修改信息：')
                add_nickname = input('请输入网站昵称(输入结束后请按‘Enter‘键)：')
                add_passw = input("请输入密码：")
                add_email = input("请输入注册邮箱(若无直接按‘Enter’键):")
                add_phone = input('请输入注册手机(若无直接按‘Enter’键):')
                account = (be_to_remove[number_to_be_removed][0], add_nickname, add_passw, add_email, add_phone)
                # print_interface((1, be_to_remove[number_to_be_removed]))

                self.__data_saved.remove(be_to_remove[number_to_be_removed])
                self.__data_saved.append(account)
                print('账号修改变化为:')
                print_interface((2, [be_to_remove[number_to_be_removed], account]))
            else:
                print('未修改数据库中的网站信息：')
        return self.__data_saved

    def search(self, website):
        returned_account_information = []
        for item in self.__data_saved:
            if website in item[0]:
                returned_account_information.append(item)
        if not returned_account_information:
            return (0, '数据库没有该网站的账号信息咩')
        return (1, returned_account_information)

    def remove(self, website):
        items = []
        for item in self.__data_saved:
            if website.strip().lower() in item[0].strip().lower():
                items.append(item)
        if not items:
            print_interface((0, '数据库中没有此网站的注册账号咩'))
        else:
            be_to_remove = {str(num): account for num, account in enumerate(items)}
            print('在数据库中搜索到的网站：')
            print_interface((1, items))
            max_num = len(items)
            remove_or_no = input('是否还要删除账号,(继续输入y,退出输入n)若输入指令错误则默认不删除:')
            if remove_or_no in ['y', 'Y']:
                number_to_be_removed = input('请输入要删除的网站账号数字0~{}:'.format(max_num - 1))
                while int(number_to_be_removed.strip()) > max_num:
                    number_to_be_removed = input('输入数字超出{}, 请重新输入：'.format(max_num))
                print('以下账号已从数据库中删除：')
                print_interface((1, be_to_remove[number_to_be_removed]))
                self.__data_saved.remove(be_to_remove[number_to_be_removed])
                return (0, (be_to_remove[number_to_be_removed], self.__data_saved))

            else:
                print('未从数据库中删除账号信息，退出')
                return (1, self.__data_saved)

    def show_all_accounts(self):
        if not self.__data_saved:
            return (0, '数据库中没有任何网站的账户咩')
        return (1, self.__data_saved)

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
