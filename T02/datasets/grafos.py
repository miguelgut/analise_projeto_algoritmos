
#Grafo com 95 nós
grafo1 = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN', 'OO', 'PP', 'QQ', 'RR', 'SS', 'TT', 'UU', 'VV', 'WW', 'XX', 'YY', 'ZZ',
                 'AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL', 'MMM', 'NNN', 'OOO', 'PPP', 'QQQ', 'RRR', 'SSS', 'TTT', 'UUU', 'VVV', 'WWW', 'XXX', 'YYY', 'ZZZ',
                 'AAAA', 'BBBB', 'CCCC', 'DDDD', 'EEEE', 'FFFF', 'GGGG', 'HHHH', 'IIII', 'JJJJ', 'KKKK', 'LLLL', 'MMMM', 'NNNN', 'OOOO', 'PPPP', 'QQQQ', 'RRRR', 'SSSS', 'TTTT', 'UUUU', 'VVVV', 'WWWW', 'XXXX', 'YYYY', 'ZZZZ'
                 ],
    'arestas': set(
        [(4, 'A', 'C'),
        (4, 'B', 'P'),
        (5, 'C', 'D'),
        (6, 'D', 'F'),
        (7, 'F', 'I'),
        (8, 'G', 'T'),
        (4, 'H', 'O'),
        (3, 'I', 'B'),
        (2, 'J', 'V'),
        (3, 'K', 'M'),
        (2, 'L', 'O'),
        (4, 'M', 'Q'),
        (6, 'N', 'R'),
        (7, 'O', 'E'),
        (9, 'P', 'D'),
        (9, 'Q', 'O'),
        (2, 'R', 'E'),
        (2, 'S', 'C'),
        (2, 'T', 'C'),
        (2, 'U', 'A'),
        (2, 'V', 'B'),
        (3, 'X', 'C'),
        (3, 'E', 'D'),
        (3, 'J', 'T'),
        (5, 'I', 'K'),
        (2, 'Q', 'F'),
        (2, 'AA', 'E'),
        (23, 'BB', 'F'),
        (45, 'CC', 'F'),
        (74, 'DD', 'C'),
        (64, 'FF', 'E'),
        (34, 'GG', 'O'),
        (75, 'HH', 'I'),
        (75, 'II', 'G'),
        (23, 'JJ', 'B'),
        (56, 'KK', 'JJ'),
        (14, 'LL', 'KK'),
        (12, 'MM', 'LL'),
        (21, 'NN', 'E'),
        (11, 'OO', 'D'),
        (10, 'PP', 'F'),
        (8, 'QQ', 'KK'),
        (6, 'RR', 'II'),
        (6, 'SS', 'DD'),
        (5, 'TT', 'FF'),
        (3, 'UU', 'CC'),
        (100, 'VV', 'BB'),
        (6, 'XX', 'ZZ'),
        (5, 'ZZ', 'A'),
        (3, 'UU', 'A'),
        (70, 'FF', 'HH'),
        (9, 'H', 'S'),
        (3, 'AAA', 'A'),
        (5, 'BBB', 'B'),
        (66, 'CCC', 'C'),
        (7, 'DDD', 'D'),
        (99, 'EEE', 'E'),
        (4, 'FFF', 'G'),
        (7, 'GGG', 'H'),
        (88, 'HHH', 'I'),
        (8, 'III', 'K'),
        (2, 'JJJ', 'L'),
        (55, 'KKK', 'M'),
        (66, 'LLL', 'N'),
        (77, 'MMM', 'AA'),
        (33, 'NNN', 'BB'),
        (23, 'OOO', 'CC'),
        (55, 'PPP', 'FF'),
        (22, 'QQQ', 'II'),
        (34, 'RRR', 'D'),
        (23, 'SSS', 'A'),
        (2, 'TTT', 'F'),
        (1, 'UUU', 'I'),
        (55, 'VVV', 'U'),
        (22, 'XXX', 'O'),
        (66, 'ZZZ', 'E'),
        (33, 'KKK', 'QQ'),
        (44, 'RR', 'KKK'),
        (55, 'W', 'V'),
        (4, 'W', 'AA'),
        (3, 'PPP', 'UUU'),
        (21, 'X', 'SSS'),
        (44, 'XX', 'N'),
        (4, 'W', 'VVV'),
        (3, 'LLL', 'FF'),
        (3, 'AAAA', 'LLL'),
        (1, 'BBBB', 'LLL'),
        (234, 'CCCC', 'AAA'),
        (55, 'DDDD', 'VV'),
        (6, 'FFFF', 'S'),
        (66, 'GGGG', 'D'),
        (7, 'HHHH', 'E'),
        (77, 'IIII', 'R'),
        (7, 'JJJJ', 'A'),
        (6, 'KKKK', 'G'),
        (3, 'LLLL', 'Q'),
        (66, 'MMMM', 'L'),
        (677, 'NNNN', 'K'),
        (77, 'OOOO', 'J'),
        (234, 'PPPP', 'H'),
        (123, 'QQQQ', 'G'),
        (234, 'RRRR', 'F'),
        (66, 'SSSS', 'E'),
        (677, 'TTTT', 'D'),
        (789, 'UUUU', 'F'),
        (78, 'VVVV', 'V'),
        (88, 'XXXX', 'B'),
        (209, 'ZZZZ', 'A'),
        (5, 'AA', 'AAA'),
        (5, 'AAA', 'A'),
        (5, 'AAA', 'AA'),
        (567, 'B', 'KKKK'),
        (223, 'DDD', 'KKKK'),
        (2321, 'VVV', 'WW'),
        (222, 'TT', 'T'),
        (112, 'E', 'TTT'),
        (232, 'RRR', 'R'),
        (4, 'O', 'OO'),
        (999, 'FF', 'F'),
        (222, 'SSS', 'SS'),
        (888, 'QQ', 'Q')
    ])
}


#Grafo com 71 nós
grafo2 = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','X','W','Z',
                 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN', 'OO', 'PP', 'QQ', 'RR', 'SS', 'TT', 'UU', 'VV', 'XX', 'ZZ',
                 'AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL', 'MMM', 'NNN', 'OOO', 'PPP', 'QQQ', 'RRR', 'SSS', 'TTT', 'UUU', 'VVV', 'XXX', 'ZZZ',
                 ],
    'arestas': set([
        (4, 'A', 'C'),
        (4, 'B', 'P'),
        (5, 'C', 'D'),
        (6, 'D', 'F'),
        (7, 'F', 'I'),
        (8, 'G', 'T'),
        (4, 'H', 'O'),
        (3, 'I', 'B'),
        (2, 'J', 'V'),
        (3, 'K', 'M'),
        (2, 'L', 'O'),
        (4, 'M', 'Q'),
        (6, 'N', 'R'),
        (7, 'O', 'E'),
        (9, 'P', 'D'),
        (9, 'Q', 'O'),
        (2, 'R', 'E'),
        (2, 'S', 'C'),
        (2, 'T', 'C'),
        (2, 'U', 'A'),
        (2, 'V', 'B'),
        (3, 'X', 'C'),
        (3, 'E', 'D'),
        (3, 'J', 'T'),
        (5, 'I', 'K'),
        (2, 'Q', 'F'),
        (2, 'AA', 'E'),
        (23, 'BB', 'F'),
        (45, 'CC', 'F'),
        (74, 'DD', 'C'),
        (64, 'FF', 'E'),
        (34, 'GG', 'O'),
        (75, 'HH', 'I'),
        (75, 'II', 'G'),
        (23, 'JJ', 'B'),
        (56, 'KK', 'JJ'),
        (14, 'LL', 'KK'),
        (12, 'MM', 'LL'),
        (21, 'NN', 'E'),
        (11, 'OO', 'D'),
        (10, 'PP', 'F'),
        (8, 'QQ', 'KK'),        
        (4, 'B', 'P'),
        (5, 'C', 'D'),
        (6, 'D', 'F'),
        (7, 'F', 'I'),
        (8, 'G', 'T'),
        (4, 'H', 'O'),
        (3, 'I', 'B'),
        (2, 'J', 'V'),
        (3, 'K', 'M'),
        (2, 'L', 'O'),
        (4, 'M', 'Q'),
        (6, 'N', 'R'),
        (7, 'O', 'E'),
        (9, 'P', 'D'),
        (9, 'Q', 'O'),
        (2, 'R', 'E'),
        (2, 'S', 'C'),
        (2, 'T', 'C'),
        (2, 'U', 'A'),
        (2, 'V', 'B'),
        (3, 'X', 'C'),
        (3, 'E', 'D'),
        (3, 'J', 'T'),
        (5, 'I', 'K'),
        (2, 'Q', 'F'),
        (2, 'AA', 'E'),
        (23, 'BB', 'F'),
        (45, 'CC', 'F'),
        (74, 'DD', 'C'),
        (64, 'FF', 'E'),
        (34, 'GG', 'O'),
        (75, 'HH', 'I'),
        (75, 'II', 'G'),
        (23, 'JJ', 'B'),
        (56, 'KK', 'JJ'),
        (14, 'LL', 'KK'),
        (12, 'MM', 'LL'),
        (21, 'NN', 'E'),
        (11, 'OO', 'D'),
        (10, 'PP', 'F'),
        (8, 'QQ', 'KK'),
        (6, 'RR', 'II'),
        (6, 'SS', 'DD'),
        (5, 'TT', 'FF'),
        (3, 'UU', 'CC'),
        (100, 'VV', 'BB'),
        (6, 'XX', 'ZZ'),
        (5, 'ZZ', 'A'),
        (3, 'UU', 'A'),
        (70, 'FF', 'HH'),
        (9, 'H', 'S'),
        (3, 'AAA', 'A'),
        (5, 'BBB', 'B'),
        (66, 'CCC', 'C'),
        (7, 'DDD', 'D'),
        (99, 'EEE', 'E'),
        (4, 'FFF', 'G'),
        (7, 'GGG', 'H'),
        (88, 'HHH', 'I'),
        (8, 'III', 'K'),
        (2, 'JJJ', 'L'),
        (55, 'KKK', 'M'),
        (66, 'LLL', 'N'),
        (77, 'MMM', 'AA'),
        (33, 'NNN', 'BB'),
        (23, 'OOO', 'CC'),
        (55, 'PPP', 'FF'),
        (22, 'QQQ', 'II'),
        (34, 'RRR', 'D'),
        (23, 'SSS', 'A'),
        (2, 'TTT', 'F'),
        (1, 'UUU', 'I'),
        (55, 'VVV', 'U'),
        (22, 'XXX', 'O'),
        (66, 'ZZZ', 'E'),
        (33, 'KKK', 'QQ'),
        (44, 'RR', 'KKK'),
        (55, 'W', 'V'),
        (4, 'W', 'AA'),
        (3, 'PPP', 'UUU'),
        (21, 'X', 'SSS'),
        (44, 'XX', 'N'),
        (4, 'W', 'VVV'),
        (3, 'LLL', 'FF'),
        (6, 'RR', 'II'),
        (6, 'SS', 'DD'),
        (5, 'TT', 'FF'),
        (3, 'UU', 'CC'),
        (100, 'VV', 'BB'),
        (6, 'XX', 'ZZ'),
        (5, 'ZZ', 'A'),
        (3, 'UU', 'A'),
        (70, 'FF', 'HH'),
        (9, 'H', 'S'),
        (3, 'AAA', 'A'),
        (5, 'BBB', 'B'),
        (66, 'CCC', 'C'),
        (7, 'DDD', 'D'),
        (99, 'EEE', 'E'),
        (4, 'FFF', 'G'),
        (7, 'GGG', 'H'),
        (88, 'HHH', 'I'),
        (8, 'III', 'K'),
        (2, 'JJJ', 'L'),
        (55, 'KKK', 'M'),
        (66, 'LLL', 'N'),
        (77, 'MMM', 'AA'),
        (33, 'NNN', 'BB'),
        (23, 'OOO', 'CC'),
        (55, 'PPP', 'FF'),
        (22, 'QQQ', 'II'),
        (34, 'RRR', 'D'),
        (23, 'SSS', 'A'),
        (2, 'TTT', 'F'),
        (1, 'UUU', 'I'),
        (55, 'VVV', 'U'),
        (22, 'XXX', 'O'),
        (66, 'ZZZ', 'E'),
        (33, 'KKK', 'QQ'),
        (44, 'RR', 'KKK'),
        (55, 'W', 'V'),
        (4, 'W', 'AA'),
        (3, 'PPP', 'UUU'),
        (21, 'X', 'SSS'),
        (44, 'XX', 'N'),
        (4, 'W', 'VVV'),
        (3, 'LLL', 'FF'),
    ])
}