nm = input()
rely = input()
need_days = input()

nm = nm.split(" ")
rely = rely.split(" ")
need_days = need_days.split(" ")

n = int(nm[0]) # all days
m = int(nm[1]) # project num

for i in range(m):
    rely[i] = int(rely[i])
    need_days[i] = int(need_days[i])


project_plan_start_list = [1 for i in range(m)] # 维护每个项目的最早开始时间
for i in range(m):
    if rely[i] == 0:
        project_plan_start_list[i] = 1
    else:
        project_plan_start_list[i] = project_plan_start_list[rely[i]-1] + need_days[rely[i]-1]

for i in range(m):
    if i < m-1:
        print(project_plan_start_list[i],end = " ")
    else:
        print(project_plan_start_list[i])

# 判断是否继续打印
max_day = 0
# 寻找最晚结束时间
for i in range(m):
    if project_plan_start_list[i] + need_days[i] > max_day:
        max_day = project_plan_start_list[i] + need_days[i]
if max_day <= (n + 1):
    project_plan_end_list = [1 for i in range(m)] # 维护最晚开始时间
    access_table = [1 for i in range(m)] # 判断这个科目是否被访问过
    for i in range(m-1,-1,-1):
        if access_table[i] == 1:
            project_plan_end_list[i] = n + 1 - need_days[i]
            j = i
            while(rely[j] != 0):
                project_plan_end_list[rely[j]-1] = project_plan_start_list[j] - need_days[j]
                j = rely[j] - 1
        else:
            continue
    for i in range(m):
        if i < m - 1:
            print(project_plan_end_list[i], end = " ")
        else:
            print(project_plan_end_list[i])


