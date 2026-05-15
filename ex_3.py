like = set(map(str, input().split(" ")))
n = int(input())
friend_like = set()
for i in range(n):
    friend_like_ind = set(map(str, input().split(" ")))
    friend_like.update(friend_like_ind)
print(len(like - friend_like))