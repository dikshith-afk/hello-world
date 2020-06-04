import re
import pandas as pd

df = pd.read_csv("/home/dikshith/Desktop/big_data_1.csv", sep=",")
msg = list(df["userText"])
xyz = []
mmsg = []


regexisEnder = r"(i?\s?do(n'?t|\s?not)\s(have|want|think)\s(so|to|this|that|it|\
anything)?|no\s(i finished|i walk|at\s?all|thank you)|is\s(of no use\
|not necessary|a small matter)|nothing|just|all this|wait|stay|end|\
(i('{0,1}m|\s{0,1}|\sam)) (done|not doing)|i?\s?(just|have)\s(can'?t|\
can\s?not|said|for now))"

# isender = re.findall(regexisEnder,str(msg)

for string in msg:
    is_ender = re.findall(regexisEnder, string)
    print(is_ender)
    xyz.append(is_ender)
    mmsg.append(string)


df_op = pd.DataFrame({"text": mmsg, "regexmatch": xyz})
df_op.to_csv("regexisender_o.csv", encoding="utf-8")
