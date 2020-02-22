#encoding=utf-8


class MatchList:
    real_index_id = -1
    name = None
    header = {}
    data = {}
    def __init__(self,index,name,header,data):
        """MatchList类初始化"""
        print("初始化已经完成")
        self.real_index_id = index
        self.name = name
        self.header = header
        self.data = data
