from hamcrest import none


def batchReplace(func):
    def inner():
        tag_word = input('输入要“目标”词 以空格隔开：')
        tag_list = tag_word.split(' ')
        print(tag_list)

        replace_word = input('输入=替换=的词 以空格隔开：')
        replace_list = replace_word.split(' ')
        print(replace_list)

        res_dict = dict(zip(tag_list, replace_list))
        print(res_dict)
        return func()
    # tmp = u'tmp.txt'
    # res = r'./res.txt'
    # with open(tmp, encoding="utf-8") as f:
    #     _res = f.read()
    #     print("目标文件内容：", _res)
    #     for i in res_dict:
    #     #     _res = _res.replace(i, res_dict[i])
    #     # print(_res)
    #     #查找字典内键值的所有位置
    #         print(_res.find(i))

    #     # with open(res, 'a', encoding="utf-8") as tag_f:
    #     #     tag_f.write('\n'+_res)

@batchReplace
def func(tag_list:list,replace_list:list,text:str):#记录单词的位置,对文本进行替换
    import re
    pos = []
    for tag_word,re_word in zip(tag_list,replace_list):
        pos.append({re_word:[i.start() for i in re.finditer(tag_word, text)]})
    # print(pos)
    dict_ = dict(zip(tag_list,pos))
    # print(dict_)
    text_list = list(text)
    for i in dict_:
        # print(i,dict_[i])
        for k in dict_[i]:
            # print(k,dict_[i][k])
            for n in dict_[i][k]:
                text_list[n]=k
    return ''.join(text_list)


        
# test 
if __name__ == "__main__":
    # batchReplace()
    tag_list = ['1','2','3']
    replace_list = ['啊啊','嗯嗯','哈~~']
    text = '1 2 31 2 31 2 31 2 31 2 31 2 31 2 3 帕秋莉go'
    res = func(tag_list,replace_list,text)
    print(res)
