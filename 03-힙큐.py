class HeapqE:
    def __init__(self):
        self.heap = []

    def heappush(self, item):  # 나옴
        self.heap.append(item)  # item 삽입
        self.siftup(len(self.heap) - 1)  # 힙 속성 유지

    def heappop(self):  # 나옴
        if not self.heap:
            print("heap empty")
            raise IndexError("pop from an empty heap")
        lastelt = self.heap.pop()  # 가장 마지막에 있는 요소 삭제
        if not self.heap:  # 힙이 비었으면( 요소가 하나밖에 없었음)
            return lastelt

        min_item = self.heap[0]  # 최소값 저장
        self.heap[0] = lastelt  # 가장 마지막 요소를 루트 자리에 넣고
        self.siftdown(0)  # 힙 재조정
        return min_item

    def heapify(self, iterable):  # 나옴
        self.heap = list(iterable)
        # for i in range(len(self.heap)//2, -1, -1)
        for i in reversed(range(len(self.heap))):
            self.siftdown(i)

    def heappushpop(self, item):  # item 추가 -> 최소값 삭제&반환
        if self.heap and item == self.heap[0]:
            item, self.heap[0] = self.heap[0], item  # item 루트 교환
            self.siftdown(0)  # 힙 조정
        return item

    # item < self.heap[0]: 삽입할 값 < 루트 : 삽입할 값이 최솟값

    def heapreplace(self, item):  # 최솟값 제거, item 추가, 최소값 반환
        if not self.heap:  # self.heap == None (빈힙이면)
            return 0
        min_item = self.heap[0]
        self.heap[0] = item  # 루트 위치에 item 삽입
        self.siftdown(0)  # 힙 재조정
        return min_item

    def nlargest(self, n):
        return sorted(self.heap, reverse=True)[:n]

    def nsmallest(self, n):
        return sorted(self.heap)[:n]

    def siftup(self, pos):  # 나옴
        child = pos
        while child > 0:  # 루트 도달할때까지
            parent = (child - 1) // 2
            if self.heap[child] < self.heap[parent]:  # 자식<부모 이면
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]  # 자식 부모 바꾸기
                child = parent
            else:  # 자식 > 부모 (힙 조정 필요 없음)
                break

    def siftdown(self, pos):  # 나옴
        end_pos = len(self.heap)
        parent = pos
        child = 2 * parent + 1

        while child < end_pos:
            right = child + 1
            if right < end_pos and self.heap[child] > self.heap[right]:  # 왼쪽자식 > 오른쪽 자식
                child = right
            if self.heap[child] < self.heap[parent]:  # 자식 < 부모
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                parent = child  # 부모 자식 위치로 이동
                child = 2 * parent + 1  # 자식 왼쪽 자식 위치로 이동
            else:  # 자식 >= 부모 이면
                break


heap = HeapqE()
heap.heapify([7, 1, 5, 9, 3])
print(heap.heap)
print(heap.heappushpop(6))
print(heap.heapreplace(2))
print(heap.heap)
print(heap.nlargest(3))
print(heap.nsmallest(3))

heap.heappush(10)
heap.heappush(5)
heap.heappush(3)
heap.heappush(8)

print('힙:', heap.heap)

print('힙 최소값 삭제:', heap.heappop())
print('힙:', heap.heap)

