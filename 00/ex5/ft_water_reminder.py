# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rishiyam <rishiyam@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/07 13:33:52 by rishiyam          #+#    #+#              #
#    Updated: 2026/09/07 13:38:36 by rishiyam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_water_reminder():
    elapsed_time = int(input("Days since last watering: "))
    if (elapsed_time > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
