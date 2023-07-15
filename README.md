# ProfessorAi
This is an AI chat application (more like a bundle of jupyter notebooks) that makes it easy to:
1. Extract text from lectures
2. Turn said text into embeddings using OpenAis ada2.0 embedding model
3. Used said embeddings to talk to gpt-3.5 or gpt-4 and get information based on lecture content

# The notebooks
## VL-Audio-retriever
This notebook splits the audio from a downloaded lecture video and then extracts the text using OpenAis opensource Whisper model.


**This requires a fair ammount of compute power**, if your machine does not have a stong GPU I reccomend renting one online or using a smaller transcription model. 

I opted for the large model since I wanted very accurate multi language transcriptions.

## Librarian
This notebook takes the finished transcript and uses OpenAis ada2.0 embedding model to turn them into embedding and store them in a Chroma vectorstorage

(It can also easily be modifed to store the vectors in pinecone online storage)

## Professor
This notebook then provides the finished experience allowing the user to "chat" with the content of the lectures and ask questions regarding material discussed.
