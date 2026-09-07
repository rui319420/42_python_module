# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rishiyam <rishiyam@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/07 12:51:53 by rishiyam          #+#    #+#              #
#    Updated: 2026/09/07 13:14:32 by rishiyam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_plot_area():
    length = input("Enter length: ")
    width = input("Enter width: ")
    area = int(length) * int(width)
    print(f"Plot area: {area}")
