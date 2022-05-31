


def div1(x,y):
    try:
        z = x / y
        return z
    except Exception as e:
        print("除法不能出现被0整除的情况")
        print(e)


print(div1(3,4))
print(div1(3,0))
print(div1(6,6))



if __name__ == '__main__':
    print(div1(3,4))