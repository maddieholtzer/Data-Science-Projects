
test = {
  'name': 'q01a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
'code': r"""
>>> model(1.0, 2.0) == 2.0
True
>>> np.all(model(3.0, np.array([4.0, 5.0])) == 3.0 * np.array([4.0, 5.0]))
True

""",
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
