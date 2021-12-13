class CuckooHashing: 
    def __init__(self, size): 
        self.M = size
        self.h = [[None, None] for x in range(size+1)]  # h-table
        self.d = [[None, None] for x in range(size+1)]  # d-table

    def hash(self, key):        # h-hash function, h(key)
        return key % self.M      
    
    def hash2(self, key):       # d-hash function, d(key)
        return (key*key % 17) *11 % self.M  
    
    def put(self, key, data): # item (key,data) 삽입위한 method
        #### 구현하시오.
        HashValue=self.hash(key)
        HashValue2=self.hash2(key)#d테이블 중복 키값 검사를 위함
        print("i=",HashValue)
        
        #중복 key 검사
        if self.h[HashValue][0]==key:#중복 key값 검사 (h테이블)
            self.h[HashValue][1]=data#data만 변경
            return
        elif self.d[HashValue2][0]==key:#중복 key값 검사 (d테이블)
            self.d[HashValue2][1]=data#data만 변경
            return

        #중복 key가 아니라면
        while True:
            if self.h[HashValue][0]==None:#h테이블이 none이라면 저장
                self.h[HashValue][0]=key
                self.h[HashValue][1]=data
                print("h-table:[",HashValue,"]",self.h[HashValue])
                
            else:#h 테이블이 none이 아니라면
                current_key=self.h[HashValue][0]#h테이블에 저장되어있는 key값 얻기
                current_data=self.h[HashValue][1]#h테이블에 저장되어있는 data 얻기
                print(self.h[HashValue],'|','h[',HashValue,']  ',end='')
            
                self.h[HashValue][0]=key#삽입
                self.h[HashValue][1]=data#삽입
            
                go_key=self.hash2(current_key)#h테이블에 저장되어 있던 key에 d-hash값
                print(self.h[HashValue],'|','h[',HashValue,']  ')
                
                if self.d[go_key][0]==None:#d테이블이 none이라면 저장
                    self.d[go_key][0]=current_key
                    self.d[go_key][1]=current_data
                    print("d-table:[",go_key,"]",self.d[go_key])
                    
                else:#d테이블 none이 아니라면
                    current_key2=self.d[go_key][0]#d테이블에 저장되어있는 key값 얻기
                    current_data2=self.d[go_key][1]#d테이블에 저장되어있는 Value값 얻기
                    print(self.d[go_key],'|','d[',go_key,']  ',end='')
                
                    self.d[go_key][0]=current_key#삽입
                    self.d[go_key][1]=current_data#삽입
                    print(self.d[go_key],'|','d[',go_key,']  ')
                    
                    HashValue=self.hash(current_key2)#d테이블에 저장되어있던 key의 h-hash값 
                    key=current_key2
                    data=current_data2
                    continue
            break
        
                                 
    def get(self, key): # key 값에 해당하는 value 값을 return 
        #### 구현하시오.
        HashValue=self.hash(key)#해당 key에 h-hash값
        HashValue2=self.hash2(key)#해당 key에 d-hash값
        
        if self.h[HashValue][0]==key:
            return self.h[HashValue][1]
        elif self.d[HashValue2][0]==key:
            return self.d[HashValue2][1]
        else:#해당 key가 없으면
            return False
         

    def delete(self, key): # key를 가지는 item 삭제
        #### 구현하시오.
        HashValue=self.hash(key)#해당 key에 h-hash값
        HashValue2=self.hash2(key)#해당 key에 d-hash값
        
        if self.h[HashValue][0]==key:#h테이블에 있다면
            self.h[HashValue][0]=None
            self.h[HashValue][1]=None
            return
        elif self.d[HashValue2][0]==key:#d테이블에 있다면
            self.d[HashValue2][0]=None
            self.d[HashValue2][1]=None
            return
        else:#해당 key가 없다면
            return False
            

    def print_table(self):
        print('********* Print Tables ************')
        print('h-table:')
            #### h-table 출력 : 구현하시오
        for i in range(len(self.h)-1):
            print(str(i).ljust(6),end='')#6칸씩 좌측 정렬
        print()
        for i in range(len(self.h)-1):
            print(str(self.h[i][0]).ljust(6),end='') #6칸씩 좌측 정렬
        print()
        #### d-table 출력 : 구현하시오 
        print('d-table:')
        for i in range(len(self.d)-1):
            print(str(i).ljust(6),end='')#6칸씩 좌측 정렬
        print()
        for i in range(len(self.d)-1):
            print(str(self.d[i][0]).ljust(6),end='') #6칸씩 좌측 정렬

if __name__ == '__main__':
    t = CuckooHashing(13)
    t.put(25, 'grape')      # 25:  12,   0
    t.put(43, 'apple')      # 43:   4,   0
    t.put(13, 'banana')     # 13:   0,   7
    t.put(26, 'cherry')     # 26:   0,   0
    t.put(39, 'mango')      # 39:   0,  10
    t.put(71, 'lime')       # 71:   9,   8
    t.put(50, 'orange')     # 50:  11,  11
    t.put(64, 'watermelon') # 64:  12,   7
    print()
    print('--- Get data using keys:')
    print('key 50 data = ', t.get(50))
    print('key 64 data = ', t.get(64))
    print()
    t.print_table() 
    print()
    print('-----  after deleting key 50 : ---------------')
    t.delete(50)
    t.print_table() 
    print()
    print('key 64 data = ', t.get(64))
    print('-----  after adding key 91 with data berry:---------------')
    t.put(91, 'berry')
    t.print_table()
    print()
    print('-----  after changing data with key 91 from berry to kiwi:---------------')
    t.put(91, 'kiwi')       # 91:  0,   9
    print('key 91 data = ', t.get(91))    
    t.print_table()
    
