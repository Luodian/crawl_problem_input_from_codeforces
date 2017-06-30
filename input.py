# coding = utf-8
import requests
from lxml import etree

# http://codeforces.com/contest/820/problem/A

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}


def crawler(contest_num,problem_num):
    url = "http://codeforces.com/contest/" + str(contest_num) + "/problem/" + problem_num
    print(url + " Veridict.")
    content = requests.get(url, headers=headers).text
    tree = etree.HTML(content)
    sample_input = tree.xpath('//div[@class = "input"]//pre/text()')
    sample_output = tree.xpath('//div[@class = "output"]//pre/text()')
    f = open('/Users/luodian/desktop/' + str(problem_num) + '.txt','w')
    print ("Sample Input: ")
    for item in sample_input:
        f.writelines(item + "\n")
        print (item)

    print ("Sample Output: ")
    for item in sample_output:
        print (item)


if __name__ == "__main__":
    c = input("Please input the contest number: ")
    for num,item in enumerate("ABCDE"):
        crawler(c,item)
