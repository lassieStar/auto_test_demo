

def setup_module():
    print("test module")
def teardowm_module():
    print("test teardowm module")
def add(a,b):
    return a+b
def test_add():
    assert add(1,1)==2
    assert add(2,5)==7

def test_add2():
    assert add(1, 1) == 2
    assert add(2, 5) == 7
    assert add(2, 3)== 5
    print("kankan")
    assert add(3,3)==6
    print("huhu")