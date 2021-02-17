"""
编写student类要求:
1.录入:学号、姓名、语文成绩、英语成绩、数学成绩
2.构造函数:计算平均成绩、总分、分数等级(90—100、60-90、0-60)
3.构造函数:学生信息分别存入数据库、.txt
"""


import pymysql

class Student():
    def __init__(self, idnum, name,chiness_score, english_score, maths_score):
        """
        初始化函数，传入学生学号 姓名 各科目成绩
        然后算平均分和总分 （如果不在这里算要在函数里算，需要再次传入这些参数，比较麻烦）
        all变量是存储在txt中的语句
        :param idnum:
        :param name:
        :param chiness_score:
        :param english_score:
        :param maths_score:
        """
        self.idnum = idnum
        self.name = name
        self.chiness_score = chiness_score
        self.english_socre = english_score
        self.maths_score = maths_score
        self.ave_score = (chiness_score + english_score + maths_score) /3
        self.total_score = chiness_score + english_score + maths_score
        self.all = '姓名： ' + self.name +' 学号' + str(self.idnum) +'英语成绩: '+ str(self.english_socre)+\
            '语文成绩: '+str(chiness_score)+ ' 数学成绩'+ str(maths_score) + '总成绩'+ str(self.total_score) +'平均分：'+str(self.ave_score)

    def print_ave_score(self):
        """平均成绩"""
        print('%s：ave_score : %s ' % (self.name,self.ave_score))

    def print_total_score(self):
        """总成绩"""
        print('%s total_score: %s ' % (self.name,self.total_score))

    def get_rank(self):
        """得到等级"""
        if self.ave_score >= 90:
            return 'A'
        elif self.ave_score >= 60:
            return 'B'
        else:
            return 'C'

    def savetxt(self):
        """存储到txt文件中"""
        file = open('student.txt','a') #a是在文件末尾追加
        file.write(self.all+"\n")  #加一个换行符号
        # file.writelines(self.all+"\n")  # 需要加一个换行符号
        file.close()
        print('%s save success' % self.name)

    def savemysql(self):
        """存储到mysql数据库"""
        db = pymysql.connect(host='数据库地址(本地localhost',user='用户名',password='密码',database='数据库名',port=3306,charset='utf8')
        cursor = db.cursor()
        cursor.execute('insert into score(idnum, name, chinese_score, english_score, maths_score, ave_score, total_score) values(%s,%s,%s,%s,%s,%s,%s)',[self.idnum, self.name, self.chiness_score, self.english_socre, self.maths_score, self.ave_score, self.total_score])
        db.commit() #需要加这个提交才可以
        cursor.close()
        db.close()
        print('%s 插入mysql成功' % self.name)
def main():
    idnum = int(input('请输入学号: '))
    name = str(input('请输入姓名:'))
    chinese_score = int(input('请输入语文成绩'))
    english_score = int(input('请输入英语成绩'))
    maths_score = int(input('请输入数学成绩'))

    student = Student(idnum,name,chinese_score,english_score,maths_score)
    student.print_ave_score()
    student.print_total_score()
    print('%s的分数等级： %s' % (student.name,student.get_rank()))
    student.savetxt()
    student.savemysql()


if __name__ == '__main__':
    main()

