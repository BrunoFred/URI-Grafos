class NodeNotFoundException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Node:
    def __init__(self, key, children=None):
        self.key = key
        self.children = children or []

    def __str__(self):
        return str(self.key)


class N_ary_Tree:

    def __init__(self):
        self.root = None
        self.size = 0

    def find_node(self, node, key):
        if node == None or node.key == key:
            return node
        for child in node.children:
            return_node = self.find_node(child, key)
            if return_node:
                return return_node
        return None

    def depth(self, key):
        node = self.find_node(self.root, key)
        if not (node):
            raise NodeNotFoundException('No element was found with the informed parent key.')
        return self.max_depth(node)

    def max_depth(self, node):
        if not (node.children):
            return 0
        children_max_depth = []
        for child in node.children:
            children_max_depth.append(self.max_depth(child))
        return 1 + max(children_max_depth)

    def add(self, new_key, parent_key=None):
        new_node = Node(new_key)
        if parent_key == None:
            self.root = new_node
            self.size = 1
        else:
            parent_node = self.find_node(self.root, parent_key)
            if not (parent_node):
                raise NodeNotFoundException('No element was found with the informed parent key.')
            parent_node.children.append(new_node)
            self.size += 1

    def print_tree(self, node, str_aux):
        if node == None: return ""
        str_aux += str(node) + '('
        for i in range(len(node.children)):
            child = node.children[i]
            end = ',' if i < len(node.children) - 1 else ''
            str_aux = self.print_tree(child, str_aux) + end
        str_aux += ')'
        return str_aux

    def is_empty(self):
        return self.size == 0

    def lenght(self):
        return self.size

    def __str__(self):
        return self.print_tree(self.root, "")

def switchingChannels (openList, closedList, forbidden, O, childList, R):
    if checkRestrictions(O-1, openList, closedList, R):
        openList.append(O-1)
        childList.append(O-1)

    if checkRestrictions(O+1, openList, closedList, R):
        openList.append(O+1)
        childList.append(O+1)

    if (O % 2) == 0:
        if checkRestrictions(O/2, openList, closedList, R):
            openList.append(O/2)
            childList.append(O/2)

    if checkRestrictions(O*2, openList, closedList, R):
        openList.append(O*2)
        childList.append(O*2)

    if checkRestrictions(O*3, openList, closedList, R):
        openList.append(O*3)
        childList.append(O*3)

    closedList.append(O)
    checkBan(childList, forbidden)
    checkBan(openList, forbidden)
    while childList:
        aux = childList.pop(0)
        if tree.find_node(tree.root, aux) == None:
            tree.add(aux, O)

def checkBan (openList, forbidden):
    for i in forbidden:
        if i in openList:
            openList.remove(i)

def checkRestrictions (value, openList, closedList, R):
    if value not in openList and value not in closedList and value > 0 and value <= R:
        return True
    else:
        return False

def checkClosedList (closedList, O):
    if O not in closedList:
        return True

while True:
    R = 10 ** 5
    openList = []
    closedList = []
    childList = []
    tree = N_ary_Tree()
    while True:
        O, D, K = [int(x) for x in input().split()]
        if (O and D and K) != 0:
            linha = input().split()
            forbidden = []
            for i in range(K):
                x = int(linha[i])
                forbidden.append(x)
            if O not in forbidden and D not in forbidden:
                break
            else:
                continue
        else:
            break
    tree.add(O)
    if not O == D == K == 0:
        while not tree.find_node(tree.root, D):
            if checkClosedList(closedList, O) == True:
                switchingChannels(openList, closedList, forbidden, O, childList, R)
                if openList:
                    O = openList.pop(0)
                else:
                    break #caso a lista esteja vazia, é que o canal destino não pode ser chegado, dai para a execução
            else:
                O = openList.pop(0)
        if tree.find_node(tree.root, D):
            print(tree.max_depth(tree.root))
        else:
            print(-1)
    if (O and D and K) != 0:
        del tree.root
    else:
        break