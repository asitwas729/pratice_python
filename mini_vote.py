voter = [] # list
candidate = {  # 후보(tuple)
        "francesca" : 0,
        "eloise" : 0
    }  

# 유권자 등록
class Voter:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.vote_count = 1
        voter.append({
            "name" : self.name,
            "password" : self.password,
            "vote_count" : self.vote_count
        })

# 유권자 검증
class VoterValid:
    def valid(self, name, password):
        for vot in voter:
            if vot["name"] == name and vot["password"] == password:
                print("로그인 성공")
                return vot
        print("로그인 실패")
        return False
    
# 투표
class Vote:
    def __init__(self, voter):
        self.voter = voter
    def vote(self, votenum):
        if self.voter.vote_count <=0:
            print("이미 투표했습니다.")
            return
        if votenum == 1:
            candidate["francesca"] += 1
            print("투표 완료")
        elif votenum == 2:
            candidate["eloise"] += 1
            print("투표 완료")
        else :
            print("잘못된 선택")
            return
        self.voter.vote_count -= 1
    def print_result(self):
        winner = max(candidate, key=candidate.get)
        print(winner)

# Test
v1 = Voter("1", "1234")
v2 = Voter("2", "1234")
v3 = Voter("3", "1234")
v4 = Voter("4", "1234")
v5 = Voter("5", "1234")
validator = VoterValid()

user = validator.valid("1", "1234")
if user:
    vote_system = Vote(v1)
    vote_system.vote(1)
    #vote_system.vote(1)  # 두 번째는 실패

user = validator.valid("5", "1234")
if user:
    vote_system = Vote(v5)
    vote_system.vote(1)
user =  validator.valid("2", "1234")
if user:
    vote_system = Vote(v2)
    vote_system.vote(1)
user = validator.valid("3", "1234")
if user:
    vote_system = Vote(v3)
    vote_system.vote(1)
user = validator.valid("4", "1234")
if user:
    vote_system = Vote(v4)
    vote_system.vote(1)

vote_system.print_result()