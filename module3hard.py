def calculate_structure_sum(args):
    sum_ = 0
    if isinstance(args, int) or isinstance(args, float):
        sum_ += args
    elif isinstance(args, str):
        sum_ += len(args)
    elif isinstance(args, dict):
        for i, j in args.items():
            sum_ += calculate_structure_sum(i)
            sum_ += calculate_structure_sum(j)
    elif isinstance(args, list) or isinstance(args, tuple) or isinstance(args, set):
        for ch in args:
            sum_ += calculate_structure_sum(ch)
    return sum_


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))