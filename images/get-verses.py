from gnt_data import get_tokens, get_tokens_by_chunk, TokenType, ChunkType
from greekutils.verse_ref import bcv_to_verse_ref

reffer = lambda x: bcv_to_verse_ref(x, start=61)


gnt_verses = get_tokens_by_chunk(TokenType.lemma, ChunkType.pericope)

pmap = dict()
with open('pericope_map.txt', 'r') as f:
    for l in f:
        p, s, e = l.split(' ')
        pmap[p] = reffer(s) + " - " + reffer(e)

commons = dict()
LIM = 15
for verse, lemma in gnt_verses.items():
    print(verse)
    verse_set = set(lemma)
    for v, l in gnt_verses.items():
        if v == verse:
            continue
        vset = set(l)
        u = verse_set.union(vset)
        intr = verse_set.intersection(vset)
        not_common = u - intr
        if len(not_common) < LIM:
            if verse in commons:
                commons[verse].append(v)
            else:
                commons[verse] = [v]
with open("common_list_pericope.txt", 'w') as g:
    for k,v in commons.items():
        print(pmap[k], file=g)
        for i in v:
            print("\t" + pmap[i], file=g)
print("DONE!")
