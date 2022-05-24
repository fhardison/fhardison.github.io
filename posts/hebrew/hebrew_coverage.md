---
title: Hebrew vocabulary statistics notes
author: Fletcher Hardison
---

# Hebrew vocabulary coverage

## Fletcher Hardson

Using code from James Tauber's `vocabulary-tools`[^tauber] and the Hebrew Bible `hebrew-vocab-tools`[^hebtools], I was able to generate the following vocabulary coverage table. 


[^tauber]: <https://github.com/jtauber/vocabulary-tools>


[^hebtools]:<https://github.com/fhardison/hebrew-vocab-tools>

This table explores what percentage of verses in the Hebrew Bible one could read once one has mastered a give number of lemmas. Note that these numbers are based on the lemmas in the verses so it is not accounting for inflected forms that might be unknown to the reader. 

If we know only 100 lemmas, then we can read less than 1% of the Hebrew Bible with 95% understanding. This isn't all that surprising considering our code reports that there are over 9,500 lemmas in the Hebrew Bible. 

**Hebrew Bible lemma coverage table**

```
           50.00%    80.00%    90.00%    95.00%   100.00%
---------------------------------------------------------
    100    90.96%    17.58%     2.73%     0.94%     0.69%
    200    95.29%    41.08%    11.09%     3.44%     1.79%
    500    98.38%    70.55%    37.60%    17.38%     9.20%
   1000    99.35%    85.13%    61.78%    37.72%    24.43%
   2000    99.83%    93.77%    81.09%    63.10%    49.86%
   5000    99.98%    98.97%    95.83%    89.25%    83.12%
    ALL   100.00%   100.00%   100.00%   100.00%   100.00%
```

Once we are comfortable with 1,000 lemmas, then we can read 37.72% with a 95% comprehension level. What is interesting is that this corresponds to the same number that Tauber reported for the Greek New Testament[^examples]; he notes that with 1,000 lemmas, one can read 37.3% of verses in the GNT. It's interesting that 1,000 Hebrew lemmas gets one slightly more verses. This is especially true considering that there are almost twice the number of lemmas in the Hebrew Bible as in the GNT. 


[^examples]: <https://github.com/jtauber/vocabulary-tools/blob/master/examples.rst>

I'm going to copy Tauber's GNT coverage table below for comparison. 

**Greek New Testament lemma coverage table**

```
           50.00%    80.00%    90.00%    95.00%    98.00%   100.00%
-------------------------------------------------------------------
    100    91.07%    13.23%     2.14%     0.66%     0.49%     0.49%
    200    96.85%    35.12%     9.87%     3.47%     2.56%     2.56%
    500    99.13%    70.88%    36.75%    17.86%    13.85%    13.84%
   1000    99.72%    88.39%    62.68%    37.30%    30.04%    30.01%
   2000    99.91%    96.61%    84.98%    65.86%    57.01%    56.97%
   5000   100.00%    99.82%    99.03%    96.86%    96.09%    96.06%
    ALL   100.00%   100.00%   100.00%   100.00%   100.00%   100.00%
```

It's interesting how the comprehension numbers drop for the Hebrew Bible compared to the GNT for at the 2,000 and 5,000 levels. This is presumably due to the number of lemmas in the respective corpora (see the table below). 5,000 lemmas is almost the all the lemmas in the GNT, but is only over half of the total in the Hebrew Bible. 


**Some basic corpus statistics**

```
               Greek   Hebrew
Hapaxlegomena  1966    3182
Total lemmas   5461    9536
% hapax        36%     33%
```

It's interesting that hapaxlegomena make up roughly the same percentage of both corpora. 

In summary, what can we conclude from these tables? Learning 5000 lemmas gets us quite a bit of both corpora, but the number of verses gained at the 95% comprehension level is lower in the Hebrew Bible simply because the sheer number of lemmas. It's also interesting how learning 1,000 lemmas creates about the same percentage of verses in both corpora. But, we also have to recognize that there are more verses in the Hebrew Bible so there is more novel texts to read at this comprehension level. 

