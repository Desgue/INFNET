def pharmacy_management():
    """Gerencia medicamentos e preços em uma farmácia"""
    medicines = {
        "Dipirona": 5.99,
        "Paracetamol": 4.50,
        "Ibuprofeno": 15.75
    }
    
    medicines["Amoxicilina"] = 25.90
    return medicines

def store_inventory():
    """Controla estoque removendo produtos"""
    inventory = {
        "Notebook": 5,
        "Mouse": 10,
        "Teclado": 7,
        "Monitor": 3
    }
    
    inventory.pop("Mouse")
    return inventory

def contact_manager():
    """Gerencia lista de contatos"""
    contacts = {
        "João": "11999887766",
        "Maria": "11988776655",
        "Pedro": "11977665544"
    }
    
    contacts["João"] = "11999887755"
    return contacts

def movie_ratings():
    """Filtra filmes com nota superior a 7"""
    movies = {
        "Inception": 8.8,
        "Matrix": 8.7,
        "Titanic": 7.8,
        "Avatar": 7.5,
        "Speed": 6.5
    }
    
    good_movies = {title: rating for title, rating in movies.items() if rating > 7}
    return good_movies

def hotel_promotions():
    """Lista quartos de hotel e suas tarifas"""
    rooms = {
        "Standard": 150.00,
        "Superior": 250.00,
        "Deluxe": 350.00,
        "Suite": 500.00
    }
    
    formatted_rooms = {room: f"R$ {price:.2f}" for room, price in rooms.items()}
    return formatted_rooms

def clothing_store_sales():
    """Gerencia vendas de uma loja de roupas"""
    sales = {}
    
    def add_sale(item, value):
        sales[item] = sales.get(item, 0) + value
    
    def remove_item(item):
        if item in sales:
            del sales[item]
    
    add_sale("Camiseta", 49.90)
    add_sale("Calça", 99.90)
    add_sale("Camiseta", 49.90)
    remove_item("Calça")
    
    return sales

def find_comprehension():
    """Recria dicionário usando comprehension"""
    return {x: x**2 for x in range(1, 10, 2)}

def access_counter(access_log):
    """Conta acessos por URL"""
    return {url: access_log.count(url) for url in set(access_log)}

def cinema_movies():
    """Converte lista de filmes para tupla"""
    movies = ["Avatar", "Matrix", "Inception", "Titanic"]
    return tuple(movies)

def book_info():
    """Cria tupla com informações do livro"""
    book = ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954]
    return tuple(book)

def pharmacy_items():
    """Gerencia conjunto de itens de farmácia"""
    items = {"Bandagens", "Vitamina C", "Protetor Solar"}
    items.add("Máscara")
    return items

def check_product_availability():
    """Verifica disponibilidade de produtos"""
    products = {"Laptop", "Mouse", "Teclado", "Monitor"}
    product_to_check = "Mouse"
    return product_to_check in products

def movie_intersection():
    """Encontra filmes assistidos em dois meses"""
    month1 = {"Matrix", "Avatar", "Inception"}
    month2 = {"Avatar", "Titanic", "Matrix"}
    return month1.intersection(month2)

def customer_preferences():
    """Gerencia preferências de cliente"""
    preferences = {"Eletrônicos", "Livros", "Roupas", "Jogos"}
    preferences.remove("Roupas")
    return preferences

def favorite_songs():
    """Gerencia conjunto de músicas favoritas"""
    songs = {"Bohemian Rhapsody", "Stairway to Heaven", 
             "Hotel California", "Sweet Child O' Mine"}
    return songs, len(songs)

def recipe_ingredients():
    """Gerencia ingredientes de uma receita"""
    ingredients = {"Farinha", "Ovos", "Leite", "Açúcar"}
    ingredients.add("Fermento")
    ingredients.remove("Açúcar")
    return ingredients

if __name__ == "__main__":
    print("\n1. Medicamentos e preços:", pharmacy_management())
    print("\n2. Estoque atualizado:", store_inventory())
    print("\n3. Lista de contatos:", contact_manager())
    print("\n4. Filmes bem avaliados:", movie_ratings())
    print("\n5. Quartos e preços:", hotel_promotions())
    print("\n6. Vendas da loja:", clothing_store_sales())
    print("\n7. Dicionário da comprehension:", find_comprehension())
    
    access_log = ["accessed: /home", "accessed: /about", 
                  "accessed: /home", "accessed: /contact", 
                  "accessed: /about", "accessed: /home"]
    print("\n8. Contagem de acessos:", access_counter(access_log))
    
    print("\n9. Tupla de filmes:", cinema_movies())
    print("\n10. Informações do livro:", book_info())
    print("\n11. Itens da farmácia:", pharmacy_items())
    print("\n12. Produto disponível:", check_product_availability())
    print("\n13. Filmes assistidos em ambos os meses:", movie_intersection())
    print("\n14. Preferências atualizadas:", customer_preferences())
    
    songs, count = favorite_songs()
    print("\n15. Músicas favoritas:", songs)
    print("Total de músicas:", count)
    
    print("\n16. Ingredientes da receita:", recipe_ingredients())
