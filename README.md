# PasswordManagement
use python to create a password management system
 ## data structure 
  * data storage :  Using  (website, nickname,password, email, phone) to store an account, 
     all accounts are packed in data structure'list'
  * a dict to store the number of characters that every item has in an account , 
     the default value of the dict is 
     {char_web: 10, char_nickname: 15, char_email: 30, char_passw: 20}
    
 ## command line parameters
 
 the programme performs  fuzzy searches(模糊搜索)
  *  website_or_show
  * -o,--option  [s, a, c, r]
    * s: search the account
    * a: add the account
    * c: change the account
    * r: remove the account
    
  
  上述website为必填参数，若show则显示数据库里存储所有的网站账号，若填网站名字，
  则执行与该网站账号相关的操作'-o,--option'为可选参数, 不选的话默认为搜索该网站下的账户
 ## examples
  * 搜索github账户：  
      1. python passw.py github
      2. python passw.py github -o s
  * 向数据库中添加github账户：python passw.py github -o a
  * 显示数据库里的所有账号: python passw.py show
  
  ## how to use this code
  1. 安装python3 [安装教程](https://blog.csdn.net/lin_not_for_codes/article/details/55096105)，教程适合win7及以上
  2. 克隆或下载该项目，若下载该项目，则解压缩下载后的项目，将passw.py文件放在 c:/users(用户)/your_pc_name,
  例如我的电脑是 c:/用户/steven
  3. 打开cmd(命令提示符)，默认在目录为：C:/Users/your_pc_name ,然后直接按照example操作即可
  
  ## 开发记录
  * 2018 09 06
    * 接下来查看历史账号和删除缓存的历史删除账号信息
    * 将账号存到腾讯微云上
  
  
  