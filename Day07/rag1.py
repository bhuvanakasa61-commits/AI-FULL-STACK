file_name="sample.txt"
with open(file_name,"r") as file:
    text=file.read()

#chunking
chunks=[]
chunk_size=100
chunk_overlap=20
step=chunk_size-chunk_overlap #100-20=80
for i in range(0,len(text),step):
    chunk=text[i:i+chunk_size] #(0-100)(80-180)(160)
    chunks.append(chunk)
for i in range(len(chunks)):
    print(f"chunk{i+1}->{chunks[i]}")

  