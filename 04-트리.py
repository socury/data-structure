class TreeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class BinaryTree:  # 이진트리
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, value):  # 삽입
        def insert_recursive(node, value):
            if not node:  # 비어있으면 새노드 생성
                return TreeNode(value)
            if value < node.value:  # 삽입할 값이 작으면
                node.left = insert_recursive(node.left, value)
            elif value > node.value:  # 삽입할 값이 크면
                node.right = insert_recursive(node.right, value)
            return node  # 중복값 넣었을 때

        self.root = insert_recursive(self.root, value)

    def search(self, value):
        def search_recursive(node, value):
            if not node:  # 못찾으면
                return False
            if node.value == value:  # 찾으면
                return True
            elif value < node.value:
                return search_recursive(node.left, value)
            elif value > node.value:
                return search_recursive(node.right, value)

        return search_recursive(self.root, value)

    def delete(self, value):  # 삭제
        def delete_recursive(node, value):
            if not node:  # 못찾으면
                return node
            if value < node.value:  # 값이 작으면
                node.left = delete_recursive(node.left, value)
            elif value > node.value:  # 값이 크면
                node.right = delete_recursive(node.right, value)
            else:  # 찾으면
                # 자식이 없는 경우
                if not node.left and not node.right:
                    return None
                # 자식이 1개인 경우
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # 자식이 2개인 경우
                temp = self.find_min(node.right)  # 오른쪽 서브트리 중에서 가장 작은값 찾기
                node.value = temp.value  # 현재 노드 값을 가장 작은값으로 교체
                node.right = delete_recursive(node.right, temp.value)  # 가장작은값 가지는 노드 삭제
            return node

        self.root = delete_recursive(self.root, value)  # 삭제 수행

    def find_min(self, node):  # 최소 값 찾기
        while node.left:
            node = node.left
        return node

    def preorder(self):  # 전위 (VRL)
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.value)  # V
                stack.append(node.right)
                stack.append(node.left)
        return result

    def inorder(self):  # 중위 (LVR)
        stack = []
        result = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)  # 현재노드 스택에 삽입
                current = current.left  # 왼쪽 자식으로 이동
            current = stack.pop()  # 스택에서 하나 빼고
            result.append(current.value)  # 결과에 출력하고
            current = current.right  # 오른쪽 자식으로 이동
        return result

    def postorder(self):  # 후위 (LRV)
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.value)  # V
                stack.append(node.left)  # L
                stack.append(node.right)  # R
        return result[::-1]


tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(20)

print("탐색 (7):", tree.search(7))
print("탐색 (17):", tree.search(17))

tree.delete(15)

print("전위 순회:", tree.preorder())
print("중위 순회:", tree.inorder())
print("후위 순회:", tree.postorder())