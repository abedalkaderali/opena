import openai


openai.api_key = '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'

def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                
                {"role": "user", "content": prompt}
            ]
            
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    while True :
        user_input = input("you:")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        
        response = get_chatgpt_response(user_input)
        print("chatbot:", response)
    

