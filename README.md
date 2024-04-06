# Zadania programistyczne nr 5

> Można korzystać z funkcji pomocniczych!
> 

Węzeł drzewa binarnego jest zdefiniowany w następujący sposób:

```python
class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Zaimplementuj zadania 1-4 korzystając z zamieszczonego kodu i uzupełniając brakujące jego fragmenty oznaczone komentarzem `#TODO`. Pobierz plik dotyczący danego zadania, uzupełnij brakujące fragmenty kodu i prześlij ten plik na UPEL tak jak do tej pory. W węzłach mogą znajdować się liczby całkowite z przedziału `[-1000, 1000]`.

### Zad.1. (15pkt)

Mając podany korzeń drzewa BST `root` odwróć drzewo i wypisz jego elementy w kolejności in-order. W tym celu zaimplementuj dwie funkcje:

- `invertTree(root: Optional[TreeNode])` - przyjmuje drzewo z korzeniem `root` i zwraca korzeń odwróconego drzewa
- `display_inorder(root: Optional[Node])` - przyjmuje korzeń drzewa BST `root`wypisz jego elementy w kolejności inorder. Elementy powinny być oddzielone od siebie spacją, po ostatnim elemencie również powinna zostać wypisana spacja.

**Przykład 1:**

Drzewo binarne:

```
    1
   / \
  2   3
     / \
    4   5

```

Odwrócona wersja tego drzewa:

```
    1
   / \
  3   2
 / \
5   4

```

W odwróconej wersji tego drzewa wszystkie lewe dzieci stają się prawymi dziećmi, a wszystkie prawe dzieci stają się lewymi dziećmi.

**Przykład 2:**

Drzewo binarne:

```
     4
    / \
   2   7
  / \ / \
 1  3 6  9

```

Odwrócona wersja tego drzewa:

```
     4
    / \
   7   2
  / \ / \
 9  6 3  1

```

Wszystkie lewe dzieci stają się prawymi dziećmi, a wszystkie prawe dzieci stają się lewymi dziećmi.

### Zad.2. (20pkt)

Mając podane dwa korzenie reprezentujące dwa drzewa binarne (`root` and `subRoot`), sprawdź czy `subRoot` jest poddrzewem `root`. W tym celu zaimplementuj 2 funkcje:

- `is_subtree(root: Optional[Node], subRoot: Optional[Node])` - zwraca true jeżeli `subRoot` jest poddrzewem `root`, w przeciwnym razie zwraca `false`.
- `is_same_tree(p: Optional[Node], q: Optional[Node])`- zwraca true jeżeli drzewa `p` i `q` są identyczne

Drzewo binarne z korzeniem w węźle `subRoot` jest poddrzewem drzewa binarnego z korzeniem w węźle `root`, jeśli `subRoot` jest węzłem w tym drzewie i wszystkie węzły z poddrzewa z korzeniem w `subRoot` są także węzłami w poddrzewie z korzeniem w `root`, oraz kolejność, struktura i wartości węzłów są zachowane. Innymi słowy, `subRoot` musi być węzłem w drzewie `root`, a każdy węzeł w poddrzewie z korzeniem w `subRoot` musi być również węzłem w poddrzewie z korzeniem w `root`. Przyjmij, że drzewo binarne jest poddrzewem samego siebie.

**Przykład 1:**

Drzewo `root`:

```
        1
       / \
      2   3
          /
         4
```

Drzewo `subRoot`:

```
      3
     /
    4

```

W pierwszym przypadku, `subRoot` jest poddrzewem `root`, ponieważ wszystkie węzły z poddrzewa `subRoot` są zawarte w drzewie `root`. 

Przykład 2:

Drzewo `root`:

```
        1
       / \
      2   3
          /
         4

```

Drzewo `subRoot`:

```
      3
     / \
    4   5

```

W drugim przypadku, `subRoot` nie jest poddrzewem `root`, ponieważ węzeł 5 z drzewa `subRoot` nie jest zawarty w poddrzewie `root`.

Przykład 3:

Drzewo `root`:

```
        1
       / \
      2   3
          /\
         4  5
        /
       6

```

Drzewo `subRoot`:

```
      3
     / \
    4   5

```

W trzecim przypadku, `subRoot` nie jest poddrzewem `root`, ponieważ węzeł 6 z drzewa `root` nie jest zawarty w poddrzewie `subRoot`.

Dwa drzewa binarne są identyczne, gdy mają te same struktury oraz każdy odpowiadający sobie węzeł ma taką samą wartość. Innymi słowy, drzewa muszą mieć te same wartości w każdym węźle i muszą być zbudowane w dokładnie takiej samej strukturze.

Przykładem dwóch identycznych drzew binarnych jest:

```
Drzewo 1:                Drzewo 2:
    1                         1
   / \                       / \
  2   3                     2   3

```

Oba drzewa mają te same wartości w węzłach (1, 2 i 3) oraz identyczną strukturę (korzeń z dwoma dzieci).

### **Zad.3. (20pkt)**

Na wejściu masz dany korzeń drzewa binarnego. Sprawdź czy dane drzewo binarne jest zbalansowane i zwróć jego wysokość. W tym celu zaimplementuj dwie funkcje:

- `get_height(root: Optional[Node])`, która zwraca wysokość drzewa z korzeniem w root
- `is_balanced(root: Optional[Node])`, która zwraca `true` jeżeli drzewo jest zbalansowane i `false` w przeciwnym przypadku

Wysokość drzewa to długość najdłuższej ścieżki od korzenia do liścia. Przyjmij, że drzewo puste ma wysokość -1, a drzewo składające się tylko z korzenia ma wysokość 0.

Drzewo binarne jest zbalansowane (zrównoważone), gdy dla każdego węzła różnica między wysokościami jego poddrzew nie przekracza jednego. Innymi słowy, dla każdego węzła w drzewie binarnym, wysokość jego lewego poddrzewa i wysokość jego prawego poddrzewa różnią się co najwyżej o 1. Drzewo puste jest zbalansowane.

Sprawdzanie czy dane drzewo jest zbalansowane można zaimplementować z użyciem funkcji sprawdzającej wysokość drzewa, jednak wtedy rozwiązanie ma złożoność kwadratową. Spróbuj zaimplementować rozwiązania o złożoności $O(n)$ gdzie n to jest liczba węzłów w drzewie. Implementacja rozwiązania w czasie liniowym może wymagać wykorzystania funkcji pomocniczej.

**Przykład 1:**

Drzewo zbalansowane o wysokości 3:

```
       10
     /    \
    5     15
   / \   /  \
  3   7 12   20

```

W tym drzewie każdy węzeł ma różnicę wysokości jego lewego i prawego poddrzewa nie większą niż 1. Na przykład, dla korzenia 10, wysokość lewego poddrzewa wynosi 2, a wysokość prawego poddrzewa wynosi 2, więc różnica wynosi 0. Podobnie dla węzła 5, wysokość lewego poddrzewa wynosi 1, a wysokość prawego poddrzewa wynosi 1, co daje różnicę 0. Ten wzorzec zachodzi dla wszystkich węzłów w drzewie, co sprawia, że jest ono zbalansowane.

**Przykład 2:**

Drzewa niezbalansowane o wysokości 3:

```
   10
    \
     15
      \
       20
```

W tym drzewie różnica wysokości lewego i prawego poddrzewa dla korzenia (10) wynosi -2, co wskazuje na brak zrównoważenia.

### **Zad.4. (20pkt)**

Na wejściu masz dany korzeń drzewa binarnego. Sprawdź czy dane drzewo binarne jest drzewem BST. W tym celu zaimplementuj metodę `is_valid_BST(root: Optional[Node])`, która przyjmuje korzeń drzewa binarnego i zwraca `true` jeżeli to drzewo jest BST oraz `false` w przeciwnym przypadku.

Drzewo binarne jest drzewem BST, gdy dla każdego węzła w drzewie, wartość węzła jest większa niż wartość wszystkich węzłów w jego lewym poddrzewie oraz mniejsza niż wartość wszystkich węzłów w jego prawym poddrzewie.