from model import SceneDataModel as D

inp = [
(22, 56),
(79, 81),
(64, 28),
(73, 42),
(73, 29),
(88, 31),
(53, 10),
(16, 33),
(55, 22),
(29, 70),
(20, 78),
(84, 30),
(74, 37),
(22, 13),
(85, 10),
(20, 13),
(65, 51),
(65, 71),
(91, 32),
(100, 13),
(53, 60),
(27, 87),
(23, 93),
(49, 16),
(94, 19),
(18, 62),
(82, 23),
(58, 64),
(46, 93),
(23, 33)
]

s = D()
s.read_input(inp)
# s.sort()
# s.greedy_init()

with open('fig3s.png', 'wb') as o:
	# o.write(s.figure_state)
	o.write(s.figure_3schemes)
