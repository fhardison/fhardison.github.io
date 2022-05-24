---
title: Means and median distance between lemma clusters
author: Fletcher Hardison
---

# Means, median distance between lemma clusters

## Fletcher Hardison 


I was reading a Koine Greek text last night and I realized that I was able to get a handle on certain new vocabulary because it was frequent within the section I was reading. I have no idea if it is frequent within the work as a whole, but the distance between encounters with the word short pretty short in the section I was reading. This got me wondering if this idea of distance would be helpful as a metric for vocabulary teaching/learning.

I wrote some code using the `gnt_data` from JTauber's [vocabulary-tools](https://github.com/jtauber/vocabulary-tools). It's available in [this gist](https://gist.github.com/fhardison/c12e0e04b4163b7c5d5d6e78ddd06d97).

The two tables below show the results of 25th-50th rows of the output. The first is sorted by mean and second by median. Looking at the output, it seems that the mean distance follows overall frequency (total). This which makes sense. It is, however, not the case for the median distance.

<figure>


lemma       mean    median    total
--------  ------  --------  -------
διά        205.5     111        666
ἵνα        207.3      91        662
ἀλλά       211.9     100        638
ἀπό        213.5     131        644
ἔρχομαι    217.6      99        631
ποιέω      241.6     105        568
τίς        243       121        554
ἄνθρωπος   247       121        550
τις        256.1     126        530
Χριστός    258.6      55        528
οὖν        261.7      94        494
εἰ         271.1     131        502
ὡς         272.8     119.5      503
ὁράω       288       129        476
κατά       292.3     127        469
μετά       292.9     149        470
μαθητής    293.4     104        262
πατήρ      321.4      76        413
ἀκούω      321.6     159.5      427
πολύς      326.2     194        415
δίδωμι     326.7     151.5      415
Παῦλος     330.8      69        158
ἡμέρα      352.1     182        389
πνεῦμα     362.8     136        379
υἱός       365.7     163        375

</figure>


Notice that the median does not follow frequency at all. The total number of occurrences and mean vary widely. The lower the median, the higher the probably that a word occurs multiple times close together. So we might expect a word like _θηρίον_ to be rare within the corpus, but in certain sections it might be common. 

<figure>


lemma        mean    median    total
---------  ------  --------  -------
Χριστός     258.6      55        528
ὅς           97.4      55       1408
ἁμαρτία     787.7      55        172
θηρίον     2618.3      55         46
οὗτος        99.1      56       1385
ὅτι         105.5      56       1294
σάββατον   1526.1      56         68
χήρα       4335.8      56         26
περιτομή   1717        56         36
πᾶς         110.5      58       1244
Ἡρῴδης     1893.6      59         43
βαπτίζω    1334.6      59.5       77
Ἰησοῦς      152        62        906
Φίλιππος   2090.9      62         36
ὀμνύω      5178.8      63         26
μή          132.4      66       1036
γάρ         132        66       1039
ἐκ          150.8      69        913
Παῦλος      330.8      69        158
κύριος      192.7      70        713
σῶμα        944.1      70        142
Πέτρος      787.5      71        156
καυχάομαι  1079.7      73         36
ἐπί         155.3      74        885
οὐαί       2878.2      74         46

</figure>

Just for kicks here is the median data, but this time showing rows 0 through 25. 

<figure>

μήτε       3885         4         34
ὁ             7         5      19769
οὔτε       1555.2       5         87
εἴτε        535.8       5         65
καί          15.3      10       8973
αὐτός        24.8      13       5546
γεννάω     1320        17         97
σύ           47.4      17       2894
ἐγώ          53.3      19       2572
ἀσπάζομαι  2151.9      22.5       59
λέγω         58.6      26       2345
ἐν           50.2      26       2733
δέ           49.4      27       2766
μέλος      3609.9      31         34
σπείρω     2319.3      34         52
εἰμί         55.9      35       2456
νόμος       622.8      36        193
ἑπτά       1492.5      40         88
οὐ           85.3      44       1605
θεός        105        45       1307
εἰς          78.1      45       1754
Αἴγυπτος   5474.6      45         25
Πιλᾶτος    1774.8      45         55
Καῖσαρ     3370.3      52         29
μνημεῖον   1768.3      53         40

</figure>


In the end is this data particularly useful? Probably not. It could be helpful as a starting point to see if a word tends to cluster. If so, then it should be possible to use `vocab-tools` to find which pericopes, paragraphs, chapters etc. where the word clusters. This could be helpful in finding readings so that we can use a familiar corpus such as the GNT to teach words that might be rare within that corpus while being more common within the wider Greek corpus. Of course this could all be hogwash. Hopefully, I can write the code to find pericopes where the words cluster.