# coding = utf-8
import requests
from lxml import etree

# http://codeforces.com/contest/820/problem/A

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}


def crawler(contest_num, problem_num):
    url = "http://codeforces.com/contest/" + str(contest_num) + "/problem/" + problem_num
    print(url + " Veridict.")
    content = requests.get(url, headers=headers).text
    tree = etree.HTML(content)
    sample_input = tree.xpath('//div[@class = "input"]//pre/text()')
    f = open('/Users/luodian/desktop/in.txt','w')
    print ("Sample Input: ")
    for item in sample_input:
        f.writelines(item + "\n")
        print (item)



if __name__ == "__main__":
    # c = input("Please input the contest number: ")
    # p = input("Please input the problem number: ")
    crawler(819, 'A')
