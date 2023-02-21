from math import ceil
class BinaryHeap:
    def __init__(self) -> None:
        self.data = []
    
    def insert(self, num: int) -> None:
        self.data.append(num)

        #heapify up
        self.__heapifyUp(len(self.data) - 1)


    def remove(self) -> None:
        if len(self.data) == 0:
            return None
        #swap root with max (last node)
        self.data[len(self.data) - 1], self.data[0] = self.data[0], self.data[len(self.data) - 1]

        out = self.data.pop()

        #heapify down
        self.__heapifyDown(0)

        return out


    def peak(self) -> int or None:
        if len(self.data) == 0:
            return None
        return self.data[0]
    
    def __heapifyUp(self, idx: int) -> None:
        
        while idx > 0 and self.data[idx] < self.data[self.getParentIdx(idx)]:
            parentIdx = self.getParentIdx(idx)
            self.data[idx], self.data[parentIdx] = self.data[parentIdx], self.data[idx]
            idx = parentIdx


    def __heapifyDown(self, idx: int) -> None:
        
        while idx < len(self.data) - 1 and self.data[idx] > self.data[self.getMinChildIdx(idx)]:
            minChildIdx = self.getMinChildIdx(idx)
            self.data[idx], self.data[minChildIdx] = self.data[minChildIdx], self.data[idx]
            idx = minChildIdx
        
    #          0
    #      1       2
    #   3    4   5   6
    def getParentIdx(self, idx: int) -> int:
        return (idx - 1) // 2
    
    def getMinChildIdx(self, idx: int) -> int:
        leftIdx = self.getLeftChildIdx(idx)
        rightIdx = self.getRightChildIdx(idx)
        if rightIdx >= len(self.data) or self.data[leftIdx] < self.data[rightIdx]:
            return leftIdx
        return rightIdx
    
    def getLeftChildIdx(self, idx: int) -> int:
        return 2 * idx + 1
    
    def getRightChildIdx(self, idx: int) -> int:
        return 2 * idx + 1

    def __len__(self):
        return len(self.data)