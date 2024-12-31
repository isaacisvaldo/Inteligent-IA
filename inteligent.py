import torch  
from transformers import GPT2LMHeadModel, GPT2Tokenizer   # type: ignore


model = GPT2LMHeadModel.from_pretrained('gpt2')  
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')  


def generate_response(prompt, max_length=50, num_return_sequences=1, do_sample=True, top_k=50, top_p=0.95, num_beams=1):  
    input_ids = tokenizer.encode(prompt, return_tensors='pt')  
    output_ids = model.generate(input_ids, max_length=max_length, num_return_sequences=num_return_sequences, do_sample=do_sample, top_k=top_k, top_p=top_p, num_beams=num_beams)  
    
    responses = [tokenizer.decode(output_id, skip_special_tokens=True) for output_id in output_ids]  
    return responses[0]  

while True:  
    user_input = input("Você: ")  
    
    if user_input.lower() in ["financas", "programacao"]:  
        response = generate_response(f"Ótimo, vamos conversar sobre {user_input}.")  
        print(f"Chatbot: {response}")  
    else:  
        response = generate_response(f"Desculpe, mas você escolheu um contexto errado. Eu posso conversar sobre finanças ou programação.")  
        print(f"Chatbot: {response}")