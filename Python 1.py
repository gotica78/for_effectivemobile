def izomorfizm(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    used_in_t = set()
    for char_s, char_t in zip(s,t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t: return False

        else:
            if s_to_t[char_t] != char_s: return False

        
            s_to_t[char_s] = char_t
            used_in_t.add(char_t)
        
        return True
    
#Оценка сложности
#Время: O(n), где n – длина строк. Один проход по строкам.
#Память: O(k), где k – количество уникальных символов. 
#В худшем случае (все символы разные) – O(n), но на практике константа ограничена алфавитом.

