
JSON = open('abilities.json')

i = 0

for line in JSON:
    print line.rstrip()
    if '{' in line:
        i+=1
        print "\t\"number\":"  + str(i) + ","


#
#
#
#
# for line in JSON.input(inplace=1, backup = '.bak'):
#     line = re.sub(r'(\"name\":\".*\",\n)', r'$1' , line)
#     print line

# for string in re.findall(pattern, JSON):
#     print string
#     print "\"number\":", ('\"' + str(i) + '\"')
