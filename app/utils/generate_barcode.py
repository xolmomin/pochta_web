from random import randint


def generate_number(prefix_num):
    def finalize(nums):
        check_sum = 0
        check_offset = (len(nums) + 1) % 2

        for i, num in enumerate(nums):
            if (i + check_offset) % 2 == 0:
                n_ = num * 2
                check_sum += n_ - 9 if n_ > 9 else n_
            else:
                check_sum += num
        return nums + [10 - (check_sum % 10)]

    so_far = prefix_num + [randint(1, 9) for _ in range(13)]
    card_number = "".join(map(str, finalize(so_far)))[:12]

    return card_number
