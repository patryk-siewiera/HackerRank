if __name__ == "__main__":
    n = int(input())
    student_marks = {}  # deklaracja dictionary
    # student_marks = {"pierwszy": [ 25, 26.5, 28 ], "drugi": [ 4, 5, 6 ], "trzeci": [ 7, 8, 9 ]}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    x1 = student_marks.get(query_name)
    x1av = sum(x1) / 3
    print("%.2f" % x1av)
