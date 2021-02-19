def arithmetic_arranger(problems, solve=False):
    arranged_problems = []
    for i in problems:
      first_number = ''
      second_number = ''
      operation = ''
      search = 0
      for j in i:
        if search == 2:
          second_number += j
        if search == 1:
          operation = j
          search+=1
        if search == 0:
          if j != ' ':
            first_number += j
          else: search += 1
        
      if second_number > first_number:
        temp = first_number
        first_number = second_number
        second_number = temp
      block = ''
      block += (5 - len(first_number)) * ' ' + first_number
      block += '\n'
      block += operation+ (4 - len(second_number)) * ' ' + second_number
      block += '\n-----\n'
      if solve:
        result = str(int(first_number) + int(second_number))
        block += (5 - len(result)) * ' ' + result
      arranged_problems.append(block)
    for i in arranged_problems:
      print(i)
    return ''