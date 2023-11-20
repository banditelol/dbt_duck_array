import random

item_list = [
    # Generate list of 10 foods
    "apple",
    "banana",
    "orange",
    "carrot",
    "potato",
    "onion",
]


def manual_generation(n_col: int = 6, n_row: int = 20) -> None:
    colnames = ["id", *[item_list[i] for i in range(n_col)]]
    print(",".join(colnames))
    for i in range(n_row):
        print(",".join([str(i), *[str(random.randint(0, 10)) for i in range(n_col)]]))


if __name__ == "__main__":
    N_COL, N_ROW = (6, 20)
    manual_generation(N_COL, N_ROW)
