class solution:
    def ismatch(self,s:str,p: str)->bool:
        p=r"{}".format(p)
        p=re.compile(p)
        if p.fullmatch(s):
            print("true")
        else:
            print("false")
