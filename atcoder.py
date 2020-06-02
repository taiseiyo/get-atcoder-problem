#!/usr/bin/env python3
import re
import urllib.request
from bs4 import BeautifulSoup


def generate_url(alphabet, num):
    url = "https://atcoder.jp/contests/abc"+num+"/tasks/abc"+num\
        + "_"+alphabet
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req)
    html = html.read().decode("utf-8")
    return html


def get_problem(html):
    target = BeautifulSoup(html, "lxml")
    text = ""
    for line in target.find_all(text=True):
        if(line[1:3] == "力例"):
            line = re.sub(r"力例 [0-9]", "力例 : ", line)
        text = text + line

    start = text.find("問題文")
    end = text.find("Score")
    return text[start+3:end]


def main():
    num = input("Enter a number above 020 : ")
    file = open("atcoder.txt", "w")
    for alphabet in ["a", "b", "c", "d"]:
        html = generate_url(alphabet, num)
        problem_string = get_problem(html)
        file.write(problem_string+"change problem\n")
    file.close()


main()
