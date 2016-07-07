# w2d: Word to Dictionary
Making a dictionary out of a word.

# Example

Showing performance of large combinations:

```
$ time python w2d.py thisisatest
  Generated 118098 combinations. Saved in thisisatest.out

  real	0m0.235s
  user	0m0.224s
  sys	  0m0.008s
```

Showing a complete example:
```
$ time python w2d.py test
  Generated 81 combinations. Saved in test.out
  
  real	0m0.015s
  user	0m0.008s
  sys	  0m0.004s

$ cat test.out | sort -r
  TEST
  TESt
  TEsT
  TEst
  TeST
  TeSt
  TesT
  Test
  tEST
  tESt
  tEsT
  tEst
  teST
  teSt
  tesT
  test
  TES7
  TEs7
  TeS7
  Tes7
  tES7
  tEs7
  teS7
  tes7
  TE5T
  TE5t
  Te5T
  Te5t
  tE5T
  tE5t
  te5T
  te5t
  TE57
  Te57
  tE57
  te57
  T3ST
  T3St
  T3sT
  T3st
  t3ST
  t3St
  t3sT
  t3st
  T3S7
  T3s7
  t3S7
  t3s7
  T35T
  T35t
  t35T
  t35t
  T357
  t357
  7EST
  7ESt
  7EsT
  7Est
  7eST
  7eSt
  7esT
  7est
  7ES7
  7Es7
  7eS7
  7es7
  7E5T
  7E5t
  7e5T
  7e5t
  7E57
  7e57
  73ST
  73St
  73sT
  73st
  73S7
  73s7
  735T
  735t
  7357
  ```
  
