# -*- coding: utf-8 -*-
import os


if __name__ == '__main__':
    wallet = []
    for price in range(1, 10000):
        p_str = str(price)
        wallet.append(p_str)
        if len(p_str) == 4:
            wallet.append(p_str[0] + ',' + p_str[1:])

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    save_file = os.path.join(BASE_DIR, 'words/maximum_amount.txt')

    with open(save_file, 'w') as f:
        f.write('\n'.join(wallet))