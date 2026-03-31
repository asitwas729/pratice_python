# list []   tuple ()    set {}  dict { : }
nums = [1,2,3,4,5,1,4]

removeRep = set(nums)   # set
list(removeRep) # 리스트로 변환
sortNum = sorted(removeRep) # sorted는 리스트로 반환한다
result = tuple(sortNum) # 튜플로 만들어서 고정시킨다.

print(result)