def star():
  """ A canvas representing a six-branches star.
      Clearly not the best canvas for a Viennese Maze.
  To see what it looks like, type:

  >>> Vmaze(** star() ).draw_quick()

  """

  return {
          'start': None,

          'goal': None,

          'canvas' :[
            (0, 2),
            (0, 3),
            (1, 2),
            (1, 7),
            (2, 3),
            (2, 6),
            (2, 7),
            (3, 4),
            (3, 5),
            (3, 6),
            (4, 5),
            (5, 11),
            (5, 10),
            (5, 6),
            (6, 7),
            (6, 9),
            (6, 10),
            (7, 8),
            (7, 9),
            (8, 9),
            (9, 10),
            (9, 12),
            (10, 11),
            (10, 12)],

          'nodes_pos':{
            0 : [0.474, 0.895],
            1 : [0.316, 0.789],
            2 : [0.421, 0.789],
            3 : [0.526, 0.789],
            4 : [0.632, 0.789],
            5 : [0.579, 0.684],
            6 : [0.474, 0.684],
            7 : [0.368, 0.684],
            8 : [0.316, 0.579],
            9 : [0.421, 0.579],
            10 : [0.526, 0.579],
            11 : [0.632, 0.579],
            12 : [0.474, 0.474]}}
