str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        # 버그 발생! 해서 self. 붙임
        print(self.str)

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()
