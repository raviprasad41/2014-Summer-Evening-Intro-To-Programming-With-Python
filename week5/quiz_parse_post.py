raw_post = "date_taken=2014-07-09&student_name_first=KKK&student_name_last=LLL&q1001=C&q1002=B"

post_list = raw_post.split("&")

for item in post_list:
    parts = item.split("=")
    item = [parts[0], parts[1]]

for item in post_list:
    print(item[0] + " = " + item[1])