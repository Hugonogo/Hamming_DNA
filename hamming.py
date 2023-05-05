with open("result.fasta") as sequencia:
  seqs = sequencia.readlines()
  i = 0
  
  while i < len(seqs):
    seqs.pop(i)
    i = i + 1
  seqs = [s.strip() for s in seqs]

comparation = str(min(seqs, key=len))
if len(comparation) != len(seqs[0]) and len(seqs)%2 == 0:
  print("Sequências não compatíveis!!!")
else:

  Hamming = []
  
  count = 0
  i = 0
  while i < len(seqs):
    for j in range(len(seqs[0])):  
      if seqs[i][j] != seqs[i+1][j]:
        count += 1
    
    Hamming.append(count)
    count = 0
    i += 2
    
    
  for i in range(len(Hamming)):
    print(f"No {i+1}ª par, a distância de Hamming é: {Hamming[i]}")
