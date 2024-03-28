import openai

# Set up your OpenAI API key
openai.api_key = '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'


def discuter_gpt3(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def générer_image(texte):
    response = openai.Image.create(
        prompt=texte,
    )
    print(response)

# Message de bienvenue
print("Bonjour! En tant qu'assistant, je suis compétent dans le design. N'hésitez pas à poser vos questions, je serai ravi de vous aider!")
print("Vous pouvez choisir de discuter ou de générer une image à partir d'un texte.")
print("Tapez 'chat' pour commencer à discuter ou 'image' pour générer une image.")
print("Tapez 'quitter' pour mettre fin à la conversation.")

while True:
    action = input("Choisissez une action : ")

    # pour quitter
    if action.lower() == 'quitter':
        print("Au revoir !")
        break
    
    # Apour discuter discussion
    if action.lower() == 'chat':
        print("Vous pouvez commencer à discuter. Tapez 'exit' pour quitter la conversation.")
        while True:
            user_input = input("Vous : ")
            if user_input.lower() == 'exit':
                print("Fin du mode discussion.")
                break
            response = discuter_gpt3(user_input)
            print("Chatbot :", response)
    
    # générer d'image
    elif action.lower() == 'image':
        texte_pour_image = input("Entrez le texte pour générer une image : ")
        url_image = générer_image(texte_pour_image)

    
    # Action invalide
    else:
        print("Action invalide. Veuillez taper 'chat' ou 'image'.")
        