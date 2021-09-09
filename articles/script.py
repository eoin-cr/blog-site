import os
import markdown

num = 37
# num represents the line number to add the html to.  To get the value of num get the line number you want to add to and minus 2


with os.scandir('.') as files:
    for entry in files:
#         print(str(entry)[-5:-2])
#         print(entry.name)
        if str(entry)[-5:-2] == ".md":
#             print("md file located honk honk")
            with open(entry.name, 'r') as f:
                text = f.read()
                html = markdown.markdown(text)

            with open("{}.html".format(entry.name[0:-3]), 'w') as f:
                f.write(html)
                print("converted markdown to html")

            with open('{}.html'.format(entry.name[0:-3]), 'r') as f:
                lines = f.readlines()
                # 4:-6 represents stripping the <h1></h1>
                title = str(lines[0])[4:-6]
                date = str(lines[1])[4:-6]
                if lines[2].startswith("<hr"):
                    prev = str(lines[2:])[17:]
                    preview = prev[:100]

                else:
                    prev = str(lines[4:])[5:]
                    preview = prev[:100]

                template = f'''<a href="articles/{entry.name[0:-3]}.html">{title}</a> <p>{date}</p>
                <p>{preview}...</p>'''
                def html_adder(tag):
                    with open(f'../{tag}.html', 'r+') as f: #r+ does the work of rw
                        lines = f.readlines()
        #                 template = f'<a href="{entry.name[0:-3]}.html">{title}</a> <p>{date}</p> <br>'
                        lines[num] = lines[num].strip() + '\n{}\n'.format(template)
                    #     lines[8] = lines[8].strip() + '\n10\n'
                        f.seek(0)
                        for line in lines:
                            f.write(line)

                if lines[3].startswith("<hr"):
                    if "tech" in lines[2]:
                        html_adder("tech")

                    if "politics" in lines[2]:
                        html_adder("politics")

                    if "complaining" in lines[2]:
                        html_adder("complaining")

            with open('../blog.html', 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
#                 template = f'<a href="{entry.name[0:-3]}.html">{title}</a> <p>{date}</p> <br>'
                lines[num] = lines[num].strip() + '\n{}\n'.format(template)
            #     lines[8] = lines[8].strip() + '\n10\n'
                f.seek(0)
                for line in lines:
                    f.write(line)

            if os.path.exists(entry.name):
              os.remove(entry.name)
            else:
              print("The file does not exist")
