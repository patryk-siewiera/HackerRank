def print_formatted(number):
    width = len("{0:b}".format(n))
    for i in range(number):
        print(
            "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(
                i + 1, width=width
            )
        )
