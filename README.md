# Personal-Package
some are created for personal and useful package

## package name: deckee

version: 0.2.3

author: YangZhiyu

author_email:Decyzy@tongji.edu.cn

### 1.save and read data
==============================================
>def save_data(var, filename, mode='normal'):

    保存用,var为需保存对象, filename为文件路径
    mode='ignore':不询问直接覆盖, mode='normal':询问后覆盖

>def read_data(filename):

    读取函数,filename为文件路径

### 2.print colorful log 
==============================================
LogPrint类:

    级别levels:
        critical > error > warning > info > debug > notset(弃用)
    输出模式modes:
        simple: 时间+级别+信息  
        normal: 时间+级别+函数名+信息
        detailed: 日期时间+级别+函数名+行号+信息
已初始化的实例log：
   > log = LogPrint('debug', 'normal')
   
    打印级别为debug及以上，输出模式为'normal'
