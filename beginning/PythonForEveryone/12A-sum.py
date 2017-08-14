def sum_func(n):
    s = 0
    for x in range(1, n + 1):
        s = s + x
        # return s #not working, maybe indentation issue
    return s

print(sum_func(10))
print(sum_func(100))

# https://www.tutorialspoint.com/python/python_functions.htm
# keep that in mind: indentation is critically important in coding Python!!!
# maybe not that critical... but,
# do not mix tabs and spaces
# http://www.secnetix.de/olli/Python/block_indentation.hawk
