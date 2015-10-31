#return true if the two given integer values are equal or their sum or difference is 5

def test_num5(x,y):
    if x==5 or y==5 or abs(x-y)==5 or (x+y)==5:
        return True
    else:
        return False

print(test_num5(7,2))
print(test_num5(5,1))
print(test_num5(3,5))
print(test_num5(3,2))
print(test_num5(3,3))
print(test_num5(1,8))
