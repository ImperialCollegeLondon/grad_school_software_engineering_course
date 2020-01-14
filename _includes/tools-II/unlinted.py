from typing import List


class Printer:
    pass


def actionate_printers(printers: List[Printer]):
    # pylint: disable=missing-docstring
    printing_actions = []
    for p in printers:

        if p == None:
            continue

        def action():
            print(p)

        printing_actions.append(action)

        p = "something"
        print(p)

    for action in printing_actions:
        action()


actionate_printers([1, 2, 2])
