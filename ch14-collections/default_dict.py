word_list = ['is', 'who', 'when', 'it', 'is', 'who', 'is']

# result = dict()

# for word in word_list:
#     if word not in result:
#         result[word] = 1
#     else:
#         result[word] += 1


# print(result)
# for word in word_list:
#     result.setdefault(word, 0)
#     result[word] += 1

# print(result)

from collections import defaultdict

result = defaultdict(int)
for word in word_list:
    result[word] += 1

print(result)


# def set_default():
#     return {'name': '', 'age': 0}

# result = defaultdict(set_default)
# print(result['a'])
