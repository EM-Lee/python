### https://en.wikibooks.org/wiki/Think_Python/Answers
### https://github.com/epequeno/ThinkPy-Solutions
### for Version 1.1.22
### current version is '2nd Edition, Version 2.2.21'

#01 How many seconds are there in 42 minutes 42 seconds?
print("Q01 -----")
m2s = 42 * 60 + 42
print("42 mins 42 secs equals to", m2s, "seconds.")
# formatted output
# http://www.python-course.eu/python3_formatted_output.php
print("42 mins 42 secs equals to {:,} seconds.".format(m2s))


#02 How many miles are there in 10 kilometers?
### Hint: there are 1.61 kilometers in a mile.
print("")
print("Q02 -----")
m2k = 10 / 1.61
print("%d kilometers is equal to %5.2f miles." %(10, m2k))


#03 If you run a 10 kilometer race in 42 minutes 42 seconds,
### what is your average pace (time per mile in minutes and seconds)?
# 10km = 6.21mi; 42m 42s = 42*60 + 42s = 2562s
# 2562 / (10 / 1.61) = 412.482s/mi
# 412.482s = 6.8747... = 6m + (.8747 * 60)s
print("")
print("Q03 -----")
secPerMile = m2s / m2k
mins, secs = divmod(secPerMile, 60)
print("My average pace is %d minutes and %d seconds per mile." \
      %(mins, secs))
### What is your average speed in miles per hour?
# v = s / t
# 1hr = 60m; 1m = 60s; 1hr = 60 * 60 = 3600s
milePerSec = m2k / m2s
milePerHr = milePerSec * 3600
print("My average speed in miles per hour is %.2f." %(milePerHr))
