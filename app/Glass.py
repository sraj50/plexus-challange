class Glass:
    def __init__(self, data):
        self.left_child: Glass = None
        self.right_child: Glass = None

        self.left_parent: Glass = None
        self.right_parent: Glass = None

        self.data = data

    # def insert(self, data):
    #     if data < self.data:
    #         if self.left_child:
    #             self.left_child.insert(data)
    #         else:
    #             self.left_child = Glass(data)
    #     elif data > self.data:
    #         if self.right_child:
    #             self.right_child.insert(data)
    #         else:
    #             self.right_child = Glass(data)
    #     else:
    #         raise ValueError("This tree does not accept duplicate values")

    @staticmethod
    def create(rows):
        for line in range(rows):
            nodes = []
            for i in range(0, line + 1):
                nodes.append(1)
            print(nodes)
        print()

    def __repr__(self):
        lines = []
        if self.right_child:
            found = False
            for line in repr(self.right_child).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.data))
        if self.left_child:
            found = False
            for line in repr(self.left_child ).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)
