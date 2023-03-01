in_ = input()
in_list = input()

in_ = in_.split(" ")
in_list = in_list.split(" ")

n = int(in_[0])
i = float(in_[1])

for j in range(n+1):
    in_list[j] = int(in_list[j])

total = 0
for j in range(n+1):
    total += in_list[j] * (1+i)**(-j)

print(total)