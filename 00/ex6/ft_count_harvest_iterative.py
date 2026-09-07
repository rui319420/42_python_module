# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rishiyam <rishiyam@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/07 13:43:13 by rishiyam          #+#    #+#              #
#    Updated: 2026/09/07 13:54:38 by rishiyam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_count_harvest_iterative():
    required_days = int(input("Days until harvest: "))
    for i in range(1, required_days + 1):
        print(f"Day {i}")
    print("Harvest time!")
