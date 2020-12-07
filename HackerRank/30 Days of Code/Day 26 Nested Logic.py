# Enter your code here. Read input from STDIN. Print output to STDOUT
returned_date = input().split(" ")
r_day = int(returned_date[0])
r_month = int(returned_date[1])
r_year = int(returned_date[2])

due_date = input().split(" ")
d_day = int(due_date[0])
d_month = int(due_date[1])
d_year = int(due_date[2])

if r_year > d_year:
    print(10000)
elif r_year < d_year:
    print(0)
else:
    if r_month != d_month:
        m_diff = r_month - d_month
        if m_diff < 0:
            print(0)
        else:
            print(500 * m_diff)
    else:
        d_diff = r_day - d_day
        if d_diff <= 0:
            print(0)
        else:
            print(15 * d_diff)
