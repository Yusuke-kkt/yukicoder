# yukicoder_no.79

the_number_of_respondents = int(input())
level_list = list(int(input())for i in range(the_number_of_respondents))

import collections
level_judge = collections.Counter(level_list)

print(level_judge.most_common()[0][0])

# collections.Counter(): 要素とその出現回数を取得
# .most_common(): ('要素', 出現回数) 形式のタプルを出現回数順に並べたリストを返す。インデックスを指定し、要素だけ、出現回数だけを取得することも可能。