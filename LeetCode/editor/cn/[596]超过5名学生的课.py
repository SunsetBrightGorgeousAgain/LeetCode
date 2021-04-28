# 有一个courses 表 ，有: student (学生) 和 class (课程)。 
# 
#  请列出所有超过或等于5名学生的课。 
# 
#  例如，表： 
# 
#  +---------+------------+
# | student | class      |
# +---------+------------+
# | A       | Math       |
# | B       | English    |
# | C       | Math       |
# | D       | Biology    |
# | E       | Math       |
# | F       | Computer   |
# | G       | Math       |
# | H       | Math       |
# | I       | Math       |
# +---------+------------+
#  
# 
#  应该输出: 
# 
#  +---------+
# | class   |
# +---------+
# | Math    |
# +---------+
#  
# 
#  
# 
#  提示： 
# 
#  
#  学生在每个课中不应被重复计算。 
#  
#  👍 198 👎 0


# There is no code of Python3 type for this problem

"select  class  from courses group by class having count(class)>=5;"

"但这里意思是一个学生可以选同一门课...无语"

"select  class  from courses group by class having count(distinct student)>=5;"