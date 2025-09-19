str_ = str(input())

newstr_ = ''
index_first = -1
index_second = -1
index_last = -1

for i in str_:
    index_first += 1
    if i.isupper():
        break

for i in range(len(str_) - 1):
    if str_[i].isdigit():
        index_second = i + 1
        break

for i in str_:
    index_last += 1
    if i == '.':
        break
        

shag = index_second - index_first

for i in range(index_first, index_last + 1, shag):
    newstr_ += str_[i]
print(newstr_)
