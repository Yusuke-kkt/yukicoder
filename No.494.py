# yukicoder_no.494

unreadable_memo = str(input())

# "yukicoder" から "?" を抜いた "unreadble_memo" と一致する文字を削除すればいい


import re
readable_memo = "yukicoder"

print(re.sub(r"[aiueo]", "", readable_memo))
