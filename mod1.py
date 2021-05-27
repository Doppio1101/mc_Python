def add(a,b):
    return a + b

def sub(a,b):
    return a - b


if __name__ == "__main__":
    print(add(1,4))
    print(sub(4,2))
# 직접 실행할 때는 mod1.py가 실행주체가 되기 때문에 위 작업이 실행된다.
# import를 하게 되면 main이 아니기때문에 실행되지않고 모듈로 사용하게 된다.
