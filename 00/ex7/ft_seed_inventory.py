# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rishiyam <rishiyam@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/07 14:30:13 by rishiyam          #+#    #+#              #
#    Updated: 2026/09/07 14:49:36 by rishiyam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_name = seed_type[0].upper() + seed_type[1:]
    if unit == "packets":
        print(f"{seed_name} seeds: {quantity} packets available.")
    elif unit == "grams":
        print(f"{seed_name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_name} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
