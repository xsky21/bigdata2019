class Calculator: # ����� ���� Ŭ����
    def __init__(self): #init�� Ŭ���� ������(constructor) ��ü ������ ���ʷ� ����Ǵ� �Լ�
        self.result = 0 #class ��� ����

    def adder(self,num): #��� �Լ�(member function)
        print("%d���� �Է� �޾ҽ��ϴ�." %num)
        self.result += num + 100 #��� ������ ����� �����ϳ� �������� ��������.
        return self.result

cal1=Calculator()
cal2=Calculator()
cal3=Calculator()
cal4=Calculator()

print(cal1.adder(3))
print(cal2.adder(4))
print(cal3.adder(3))
print(cal4.adder(7))
