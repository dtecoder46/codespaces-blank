def key(input_list, keyword):
    write = open("data.xml", "a")
    if input_list[0] == keyword:
        xml = "<" + input_list[1] + ">\n" + "</" + input_list[1] + ">"
        write.write(xml)

def loop(input_list):
    keywords = ["create:db", "delete:db", "create:tb", "delete:tb", "inject:tb", "get:tb"]
    for keyword in keywords:
        key(input_list, keyword)

read = open("comm.xql", "r")
input = read.read()
read.close()

if input.find(" = ") != -1:
    input_list = input.split(" = ")
    loop(input_list)