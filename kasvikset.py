hedelmat = {"banaanni","omena", "tomaatti","kirsikka"}
vihannekset = {"tomaatti","peruna","porkkana","munakoiso"}
marjat = {"mustikka","mansikka","kirsikka","munakoiso"}
print(hedelmat.intersection(marjat))
print(vihannekset.difference(hedelmat))
print(hedelmat.union(vihannekset,marjat))
hed_mar = hedelmat.union(marjat).difference(vihannekset)
print(hed_mar)
vain_hed = hedelmat.difference(vihannekset|marjat)
vain_viha = vihannekset.difference(hedelmat| marjat)
vain_mar = marjat.difference(vihannekset|hedelmat)
print(vain_hed.union(vain_mar|vain_viha))