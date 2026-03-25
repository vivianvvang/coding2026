class HtmlLabel:
    def __init__(self, text):
        self.text = text
        self.children = None

class Solution:
    def sameWordOfHtmlLabels(self, root1, root2):
        str1 = self.getLeafConcatenation(root1)
        str2 = self.getLeafConcatenation(root2)
        return str1 == str2

    def getLeafConcatenation(self, root):
        if root is None:
            return ""

        result = []
        stack = []
        stack.append(root)

        while stack:
            current = stack.pop()

            # If it's a leaf node (has text and no children or empty children)
            if (current.text is not None and current.text != "" and 
                (current.children is None or len(current.children) == 0)):
                result.append(current.text)

            # Add children to stack in reverse order for left-to-right traversal
            # Then order is correct after pop()

            if current.children is not None:
                for i in range(len(current.children) - 1, -1, -1):
                    if current.children[i] is not None:
                        stack.append(current.children[i])

        return "".join(result)

def main():
    test1()
    test2()
    test3()
    test4()
    test5()

def test1():
    print("===== Test 1: =====")

    # Label 1:
    # <root>
    #     <container>
    #         <div> "He" </div>
    #         <div> "llo" </div>
    #     </container>
    #     <p> "World" </p>
    # </root>

    he = HtmlLabel("He")
    llo = HtmlLabel("llo")
    container1 = HtmlLabel(None)
    container1.children = [he, llo]

    world = HtmlLabel("World")
    label1 = HtmlLabel(None)
    label1.children = [container1, world]

    # Label 2:
    # <root>
    #     <div> "Hello" </div>
    #     <container>
    #         <span> "Wor" </span>
    #         <span> "ld" </span>
    #     </container>
    # </root>

    wor = HtmlLabel("Wor")
    ld = HtmlLabel("ld")
    container2 = HtmlLabel(None)
    container2.children = [wor, ld]

    hello = HtmlLabel("Hello")
    label2 = HtmlLabel(None)
    label2.children = [hello, container2]

    res1 = Solution().sameWordOfHtmlLabels(label1, label2)
    print(res1)  # Expected: true

def test2():
    print("===== Test 2: =====")

    # Label 1:
    # <root>
    #     <div> "Hello" </div>
    #     <div> "World" </div>
    # </root>

    hello = HtmlLabel("Hello")
    world = HtmlLabel("World")
    label1 = HtmlLabel(None)
    label1.children = [hello, world]

    # Label 2:
    # <root>
    #     <div> "Hello" </div>
    #     <div> "Earth" </div>
    # </root>

    hello2 = HtmlLabel("Hello")
    earth = HtmlLabel("Earth")
    label2 = HtmlLabel(None)
    label2.children = [hello2, earth]

    res2 = Solution().sameWordOfHtmlLabels(label1, label2)
    print(res2)  # Expected: false

def test3():
    print("===== Test 3: =====")

    # Label 1:
    # <root>
    #     <section>
    #         <div>
    #             <span> "A" </span>
    #             <span> "B" </span>
    #         </div>
    #         <p> "C" </p>
    #     </section>
    #     <footer>
    #         <div> "D" </div>
    #         <div>
    #             <span> "E" </span>
    #             <span> "F" </span>
    #         </div>
    #     </footer>
    # </root>

    a = HtmlLabel("A")
    b = HtmlLabel("B")
    divInSection = HtmlLabel(None)
    divInSection.children = [a, b]

    c = HtmlLabel("C")
    section = HtmlLabel(None)
    section.children = [divInSection, c]

    e = HtmlLabel("E")
    f = HtmlLabel("F")
    divInFooter = HtmlLabel(None)
    divInFooter.children = [e, f]

    d = HtmlLabel("D")
    footer = HtmlLabel(None)
    footer.children = [d, divInFooter]

    label1 = HtmlLabel(None)
    label1.children = [section, footer]

    # Label 2:
    # <root>
    #     <div> "AB" </div>
    #     <section>
    #         <p> "C" </p>
    #         <div> "DEF" </div>
    #     </section>
    # </root>

    c2 = HtmlLabel("C")
    def_ = HtmlLabel("DEF")
    sectionTree2 = HtmlLabel(None)
    sectionTree2.children = [c2, def_]

    ab = HtmlLabel("AB")
    label2 = HtmlLabel(None)
    label2.children = [ab, sectionTree2]
    res3 = Solution().sameWordOfHtmlLabels(label1, label2)
    print(res3)  # Expected: true

def test4():
    print("===== Test 4: =====")

    # Label 1:
    # <root>
    #     <div> "Hello" </div>
    #     <div> "World" </div>
    #     <div> "Test" </div>
    # </root>

    hello = HtmlLabel("Hello")
    world = HtmlLabel("World")
    test = HtmlLabel("Test")
    label1 = HtmlLabel(None)
    label1.children = [hello, world, test]

    # Label 2:
    # <root>
    #     <div> "HelloWorld" </div>
    # </root>

    helloWorld = HtmlLabel("HelloWorld")
    label2 = HtmlLabel(None)
    label2.children = [helloWorld]

    res4 = Solution().sameWordOfHtmlLabels(label1, label2)
    print(res4)  # Expected: false

def test5():
    print("===== Test 5: =====")

    # Label 1: null (empty tree)
    label1 = None

    # Label 2:
    # <root>
    #     <div> "test" </div>
    # </root>

    testNode = HtmlLabel("test")
    label2 = HtmlLabel(None)
    label2.children = [testNode]

    res5 = Solution().sameWordOfHtmlLabels(label1, label2)
    print(res5)  # Expected: false

if __name__ == "__main__":
    main()