python file_name="sample.txt"
with open(file_name,"r") as file:
    text=file.read()

#chunking
chunks=[]
chunk_size=100
for i in range(0,len(text),chunk_size):
    chunk=text[i:i+chunk_size]
    chunks.append(chunk)
for i in range(len(chunks)):
    print(f"chunk{i+1}->{chunks[i]}")