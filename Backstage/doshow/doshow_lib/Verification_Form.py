# -*- coding: utf-8 -*-
import re

class Form_verification:
    def __init__(self,a):
        self.a = a
    def phone_V(self):
        if len(self.a) == 11:
            b = re.match('^[1][3,4,5,7,8]\d+$',self.a)
            if b:
                return True
            else:
                return False
        else:
            return False
    def username_V(self,min_num,max_num):
        # The username can be ( a-z 0-9 A-Z _ )
        if len(self.a) >= min_num and len(self.a) <= max_num:
            b = re.match('^[a-zA-Z]\w+[a-zA-Z0-9]$',self.a)
            if b:
                return True
            else:
                return False
        else:
            return False

    def password_V(self,min_num,max_num,complexity):
        # complexity为“数字0”代表没有复杂度要求，为其他值代表有复杂度要求，复杂度要求是“字母数字符号组合”
        # The password can be ( / \ + = _ - ! @ # $ % ^ & * . , : ; ` " ' | )
        if len(self.a) >= min_num and len(self.a) <= max_num:
            if complexity == 0:
                b = re.match('^[0-9a-zA-z\+\-_=!\?%/\*#@&\^\$\.\,:;`\"\'\|]+$',self.a)
                if b:
                    return True
                else:
                    return False
            else:
                b = re.match('^[0-9a-zA-z\+\-_=!\?%/\*#@&\^\$\.\,:;`\"\'\|]+$',self.a)
                if b:
                    c1 = re.findall('[0-9]',self.a)
                    c2 = re.findall('[a-zA-Z]',self.a)
                    c3 = re.findall('[\+\-_=!\?%/\*#@&\^\$\.\,:;`\"\'\|]',self.a)
                    if len(c1) > 0 and len(c2) > 0 and len(c3) > 0:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False