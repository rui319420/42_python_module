# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rishiyam <rishiyam@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/07 13:24:09 by rishiyam          #+#    #+#              #
#    Updated: 2026/09/07 13:40:27 by rishiyam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_plant_age():
    elapsed_days = int(input("Enter plant age in days: "))
    if (elapsed_days > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to glow.")
