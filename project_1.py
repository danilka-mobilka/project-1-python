from random import randrange

def display_board(board):
    """Виводить поточний стан дошки"""
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    """Обробляє хід користувача"""
    free_fields = make_list_of_free_fields(board)
    
    while True:
        try:
            move = int(input("Введіть номер поля для вашого ходу (O): "))
            if move < 1 or move > 9:
                print("Число має бути від 1 до 9!")
                continue
                
            # Знаходимо координати за номером
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            if (row, col) in free_fields:
                board[row][col] = 'O'
                break
            else:
                print("Це поле вже зайняте! Оберіть інше.")
        except ValueError:
            print("Будь ласка, введіть ціле число!")

def make_list_of_free_fields(board):
    """Повертає список вільних полів"""
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    """Перевіряє, чи є переможець"""
    # Перевірка рядків
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
    
    # Перевірка стовпців
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    
    # Перевірка діагоналей
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    
    return False

def draw_move(board):
    """Виконує хід комп'ютера"""
    free_fields = make_list_of_free_fields(board)
    
    if free_fields:
        # Випадковий вибір з вільних полів
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def main():
    """Основна функція гри"""
    # Ініціалізація дошки
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print("Гра в Хрестики-Нулики!")
    print("Комп'ютер грає за X, ви граєте за O")
    print("Комп'ютер робить перший хід...")
    
    # Перший хід комп'ютера в центр
    board[1][1] = 'X'
    display_board(board)
    
    # Основний цикл гри
    for _ in range(4):  # Максимум 4 ходи після першого
        # Хід користувача
        print("\nВаш хід:")
        enter_move(board)
        display_board(board)
        
        # Перевірка перемоги користувача
        if victory_for(board, 'O'):
            print("Вітаю! Ви виграли!")
            return
        
        # Перевірка на нічию
        free_fields = make_list_of_free_fields(board)
        if not free_fields:
            print("Нічия!")
            return
        
        # Хід комп'ютера
        print("\nХід комп'ютера:")
        draw_move(board)
        display_board(board)
        
        # Перевірка перемоги комп'ютера
        if victory_for(board, 'X'):
            print("Комп'ютер виграв!")
            return
        
        # Перевірка на нічию
        free_fields = make_list_of_free_fields(board)
        if not free_fields:
            print("Нічия!")
            return

if __name__ == "__main__":
    main()
