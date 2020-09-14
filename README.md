# My-Work


1)Specify the filepath appropriately! This will be the directory from where you'll want to remove the duplicates.<br>
2)In case of mobiles where "-1" is the extension instead of "-Copy", in that case the regex code(just a single line) should be a bit modified to
x = re.compile(r'(.*)- 1.jpg')
instead of
x = re.compile(r'(.*)- Copy.jpg')

