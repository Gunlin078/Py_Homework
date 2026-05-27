class AlchemistGame:
    def __init__(self):
        # Доступные рецепты: (элемент1, элемент2) -> результат
        self.recipes = {
            ("вода", "огонь"): "пар",
            ("огонь", "вода"): "пар",
            
            ("огонь", "земля"): "лава",
            ("земля", "огонь"): "лава",
            
            ("вода", "земля"): "грязь",
            ("земля", "вода"): "грязь",
            
            ("воздух", "вода"): "туман",
            ("вода", "воздух"): "туман",
            
            ("воздух", "огонь"): "энергия",
            ("огонь", "воздух"): "энергия",
            
            ("земля", "воздух"): "пыль",
            ("воздух", "земля"): "пыль",
            
            ("пар", "вода"): "облако",
            ("вода", "пар"): "облако",
            
            ("лава", "вода"): "камень",
            ("вода", "лава"): "камень",
            
            ("энергия", "вода"): "жизнь",
            ("вода", "энергия"): "жизнь",
            
            ("жизнь", "земля"): "растение",
            ("земля", "жизнь"): "растение",
            
            ("растение", "огонь"): "пепел",
            ("огонь", "растение"): "пепел",
            
            ("камень", "огонь"): "металл",
            ("огонь", "камень"): "металл",
            
            ("металл", "воздух"): "инструмент",
            ("воздух", "металл"): "инструмент",
            
            ("инструмент", "дерево"): "доска",
            ("дерево", "инструмент"): "доска",
            
            ("доска", "доска"): "дом",
        }
        
        # Начальные элементы
        self.elements = ["вода", "огонь", "земля", "воздух"]
        
        # Кэш комбинаций для быстрого поиска
        self.combination_cache = {}
        for (a, b), result in self.recipes.items():
            self.combination_cache[(a, b)] = result
            self.combination_cache[(b, a)] = result  # порядок не важен
    
    def show_elements(self):
        """Показать все имеющиеся элементы"""
        if not self.elements:
            print("У вас нет элементов!")
        else:
            print("\n Ваши элементы:")
            for i, elem in enumerate(self.elements, 1):
                print(f"  {i}. {elem.capitalize()}")
            print(f"  Всего: {len(self.elements)} элементов")
    
    def show_help(self):
        """Показать подсказки"""
        print("\n" + "="*50)
        print("УПРАВЛЕНИЕ:")
        print("  • Введите два элемента через пробел (например: вода огонь)")
        print("  • 'список' - показать все элементы")
        print("  • 'рецепты' - показать доступные рецепты")
        print("  • 'сброс' - начать заново")
        print("  • 'выход' - выйти из игры")
        print("="*50)
    
    def show_recipes(self):
        """Показать все возможные рецепты из имеющихся элементов"""
        possible = set()
        for i, a in enumerate(self.elements):
            for b in self.elements[i:]:  # проверяем все пары
                if (a, b) in self.combination_cache:
                    result = self.combination_cache[(a, b)]
                    if result not in self.elements:
                        possible.add((a, b, result))
        
        if possible:
            print("\n Доступные комбинации:")
            for a, b, result in sorted(possible):
                print(f"  • {a.capitalize()} + {b.capitalize()} = {result.capitalize()}")
        else:
            print("\n Пока нет доступных комбинаций! Попробуйте создать больше элементов.")
    
    def combine(self, elem1, elem2):
        #Попытаться объединить два элемента
        # Приводим к нижнему регистру
        elem1 = elem1.lower()
        elem2 = elem2.lower()
        
        # Проверяем, есть ли такие элементы у игрока
        if elem1 not in self.elements:
            print(f" У вас нет элемента '{elem1.capitalize()}'!")
            return False
        
        if elem2 not in self.elements:
            print(f" У вас нет элемента '{elem2.capitalize()}'!")
            return False
        
        # Ищем рецепт
        if (elem1, elem2) in self.combination_cache:
            result = self.combination_cache[(elem1, elem2)]
            
            # Проверяем, не открыли ли мы уже этот элемент
            if result in self.elements:
                print(f" {elem1.capitalize()} + {elem2.capitalize()} = {result.capitalize()} (уже есть)")
                return False
            
            # Добавляем новый элемент
            self.elements.append(result)
            print(f"\n ПОЗДРАВЛЯЮ! ")
            print(f"   {elem1.capitalize()} + {elem2.capitalize()} = {result.capitalize()}")
            print(f"   Вы создали: {result.capitalize()}!")
            return True
        else:
            print(f" {elem1.capitalize()} и {elem2.capitalize()} вместе ничего не дают :(")
            return False
    
    def reset(self):
        """Сбросить игру"""
        self.elements = ["вода", "огонь", "земля", "воздух"]
        print("\n Игра сброшена! Начинаем с 4 базовых элементов.")
    
    def play(self):
        """Основной игровой цикл"""
        print("\n" + "="*50)
        print("️ ДОБРО ПОЖАЛОВАТЬ В ИГРУ 'АЛХИМИК' ️")
        print("="*50)
        print("Начните с 4 базовых элементов: Вода, Огонь, Земля, Воздух")
        print("Смешивайте их, чтобы открывать новые элементы!")
        
        self.show_help()
        
        while True:
            print("\n" + "-"*50)
            self.show_elements()
            
            command = input("\n Ваш ход: ").strip().lower()
            
            if command == "выход":
                print("\n До свидания! Возвращайтесь снова!")
                break
            
            elif command == "список":
                continue  # уже показали элементы
            
            elif command == "рецепты":
                self.show_recipes()
            
            elif command == "сброс":
                self.reset()
            
            elif command == "помощь":
                self.show_help()
            
            else:
                # Пытаемся распарсить два элемента
                parts = command.split()
                if len(parts) == 2:
                    self.combine(parts[0], parts[1])
                else:
                    print(" Непонятная команда!")
                    print("   Введите два элемента через пробел или 'помощь'")
            
            # Проверка на победу
            if len(self.elements) >= 15:  # условная победа
                print("\n" + "="*50)
                print(" ПОБЕДА! ")
                print("Вы создали множество элементов и доказали своё мастерство!")
                print(f"Всего открыто элементов: {len(self.elements)}")
                print("="*50)
                
                again = input("\nХотите сыграть ещё раз? (да/нет): ").lower()
                if again == "да" or again == "д":
                    self.reset()
                    continue
                else:
                    print("\n Спасибо за игру!")
                    break


# Запуск игры
if __name__ == "__main__":
    game = AlchemistGame()
    game.play()
