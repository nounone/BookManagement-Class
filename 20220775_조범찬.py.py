import sys

class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"  ID: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판연도: {self.year}"

class Node:  
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next
    
    def append(self, new):  
        if new is not None:
            new.link = self.link
            self.link = new
            
    def popNext(self): 
        deleted_node = self.link
        if deleted_node is not None: 
            self.link = deleted_node.link
        return deleted_node

class LinkedList:  
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def getNode(self, pos):
        if pos < 0: return None
        ptr = self.head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr

    def insert(self, pos, elem):
        node = Node(elem, None)  
        before = self.getNode(pos - 1)
        if before == None: 
            node.link = self.head
            self.head = node
        else:  
            before.append(node)

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None: 
            if self.head is not None:
                deleted_node = self.head
                self.head = self.head.link
                return deleted_node
            else: return None
        else:  
            return before.popNext()

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count

    def find_by_title(self, title): 
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data  
            ptr = ptr.link
        return None  

    def find_pos_by_title(self, title): 
        ptr = self.head
        pos = 0
        while ptr is not None:
            if ptr.data.title == title:
                return pos  
            ptr = ptr.link
            pos += 1
        return -1  

    def find_by_id(self, book_id):
        ptr = self.head
        while ptr is not None:
            if ptr.data.book_id == book_id:
                return ptr.data  
            ptr = ptr.link
        return None  
    
    def display(self):
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.") 
            return
            
        print("--- 전체 도서 목록 ---")
        ptr = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.link
        print("--------------------")

class BookManagement:
    def __init__(self):
        self.book_list = LinkedList()  # 저장 리스트

    def add_book(self, book_id, title, author, year):
        if self.book_list.find_by_id(book_id) is not None:
            print(f"오류: 책 번호 '{book_id}'는(은) 이미 존재합니다.") 
        else:
            new_book = Book(book_id, title, author, year)
            self.book_list.insert(0, new_book)
            print("도서가 성공적으로 추가되었습니다.")

    def remove_book(self, title):
        pos = self.book_list.find_pos_by_title(title)
        
        if pos == -1:
            print(f"오류: '{title}' 제목의 도서를 찾을 수 없습니다.") 
        else:
            self.book_list.delete(pos)
            print(f"'{title}' 도서가 성공적으로 삭제되었습니다.")

    def search_book(self, title):
        book = self.book_list.find_by_title(title)
        
        if book is None:
            print(f"오류: '{title}' 제목의 도서를 찾을 수 없습니다.")
        else:
            print("--- 도서 조회 결과 ---")
            print(book)
            print("--------------------")

    def display_books(self):
        self.book_list.display() 

    def run(self):
        while True:
            print("\n===== 도서 관리 프로그램 =====")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")
            print("============================")
            
            choice = input("메뉴를 선택하세요: ")

            if choice == '1': # 1. 도서 추가 
                book_id = input("책 번호: ")
                title = input("책 제목: ")
                author = input("저자: ")
                year = input("출판 연도: ")
                self.add_book(book_id, title, author, year)

            elif choice == '2': # 도서 삭제
                title = input("삭제할 책 제목: ")
                self.remove_book(title)

            elif choice == '3': # 도서 조회
                title = input("조회할 책 제목: ")
                self.search_book(title)

            elif choice == '4': # 전체 출력
                self.display_books()

            elif choice == '5':  # 종료
                print("프로그램을 종료합니다.") 
                sys.exit()

            else:
                print("잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.") 

if __name__ == "__main__":
    app = BookManagement()
    app.run()