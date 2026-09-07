# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rishiyam <rishiyam@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/07 13:17:16 by rishiyam          #+#    #+#              #
#    Updated: 2026/09/07 13:40:22 by rishiyam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_harvest_total():
    D1 = int(input("Day 1 harvest: "))
    D2 = int(input("Day 2 harvest: "))
    D3 = int(input("Day 3 harvest: "))
    total = D1 + D2 + D3
    print(f"Total harvest: {total}")
