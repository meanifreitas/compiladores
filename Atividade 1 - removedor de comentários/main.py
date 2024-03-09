import re # used for regex

def remove_comments(code):
  comments = []
  # finds comments like // and /* */ 
  comments.append(re.findall(r'//.*$', code, flags=re.MULTILINE))
  comments.append(re.findall(r'/\*.*?\*/', code, flags=re.DOTALL))

  # removes comments like // until the end of the line
  code = re.sub(r'//.*$', '', code, flags=re.MULTILINE)
  # re.sub receives the following arguments:
  # the regular expression
  # the string to be searched
  # the string to be replaced
  # the re.MULTILINE flag allows the pattern to be found in all lines
  
  # removes comments like /* */
  code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
  # the re.DOTALL allows the pattern to be replaced in all lines
  
  return code, comments

def main():
  with open('input.txt', 'r') as file:
    code = file.read()
  code, comments = remove_comments(code)
  
  with open('output.txt', 'w') as file:
    file.write(code)

  with open('comments.sco', 'w') as file:
    for line in comments:
      for comment in line:
        file.write(comment + '\n')

if __name__ == "__main__":
  main()