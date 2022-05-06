def func():
    global global_var
    local_var = "지역 변수"
    print(local_var)
    print(global_var)
    

global_var = "전역 변수"
func()
print(global_var)
