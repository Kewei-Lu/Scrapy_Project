def time_find(job_list,job_no):
    for i in range(2 * int(job_no)-1):
        if job_list[i][1] == job_no and job_list[i][2] == 0:
            start_time = job_list[i][0]
            job_list.remove(job_list[i])
            #print(job_list)
        if job_list[i][1] == job_no and job_list[i][2] == 1:
            end_time = job_list[i][0]
            job_list.remove(job_list[i])
            #print(job_list)
    #print(int(end_time) - int(start_time))
            return int(end_time) - int(start_time)


number = int(input())
job_list = []
job_time_list = []
# number = 8
# job_list = [[1,1,0],[5,2,0],[10,3,0],[20,3,1],[25,4,0],[40,4,1],[1000,2,1],[2000,1,1]]
# job_time_list = []
for i in range(number):
    job_list.append(input().split(' '))
for i in range(number):
    job_list[i][0] = int(job_list[i][0])
    job_list[i][1] = int(job_list[i][1])
    job_list[i][2] = int(job_list[i][2])
#
for i in range(number // 2,0,-1):
    job_time = time_find(job_list,i)
    job_time_list.append([i,job_time])
for i in range(number//2-1,0,-1):
    count = i-1
    #print(count)
    while count>=0:
        job_time_list[i][1] -= job_time_list[count][1]
        count-=1
job_time_list.sort(key = lambda x:x[1],reverse=True)
print(job_time_list[0][0])