# w2d: Word to Dictionary
Making a dictionary out of a word.

# Example

Showing performance of large combinations:

```
$ time python w2d.py thisisatest
  Generated 118098 combinations. Saved in thisisatest.out
  
  real	0m0.356s
  user	0m0.348s
  sys	0m0.004s 
```

Showing a complete example:
```
$ time python w2d.py test
  Generated 81 combinations. Saved in test.out
  
  real	0m0.015s
  user	0m0.008s
  sys	0m0.004s

$ cat test.out
  73S7
  t3S7
  TE5T
  TeS7
  te57
  7Est
  t3st
  7E57
  T3S7
  7e5T
  7es7
  teSt
  tesT
  73sT
  735t
  TEST
  Test
  teST
  tEst
  t357
  tESt
  7eST
  T35t
  73s7
  TE57
  teS7
  7ESt
  t3sT
  tE5T
  TEsT
  7e5t
  T3sT
  7esT
  735T
  t3s7
  TEst
  TeST
  tES7
  tE5t
  T357
  TE5t
  73St
  7Es7
  TesT
  7eSt
  Te5t
  TEs7
  TES7
  t35T
  7E5t
  tE57
  test
  tEsT
  73ST
  t35t
  7357
  TESt
  Tes7
  tEST
  T3ST
  T35T
  t3ST
  Te5T
  73st
  te5T
  7eS7
  7EST
  7est
  t3St
  7e57
  T3St
  7E5T
  T3st
  7ES7
  T3s7
  tEs7
  7EsT
  TeSt
  tes7
  te5t
  Te57
  ```
  
