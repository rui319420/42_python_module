# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rishiyam <rishiyam@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/07 13:55:56 by rishiyam          #+#    #+#              #
#    Updated: 2026/09/07 14:29:03 by rishiyam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def display_days(n):
    if n <= 0:
        return
    else:
        display_days(n - 1)
        print(f"Day {n}")


def ft_count_harvest_recursive():
    required_days = int(input("Days until harvest: "))
    display_days(required_days)
    print("Harvest time!")
