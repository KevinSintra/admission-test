import my_package.question1
import my_package.question2

#question3
# What is GIT and why is it used?
    # 過去在做電子文書處理時，如果要回到過去的版本，只能將檔案複製一份，並將檔名加上版本號，如：test_1.0.doc、test_1.1.doc、test_1.2.doc
    # Git 簡單用可以讓使用者在做電子文書處理時，可隨時回到過去的版本並查看過去的版本差異
    # Git 重點是多人開發專案時，可以讓多人同時開發同一個專案時，避免發生版本衝突。或者管理擁有多個產品線的專案
    # 有了 Git 對在開源軟體上有更好的協作效率，讓世界上的開發者可以更快速的開發出更好的軟體
# What is difference between List, Dictionary, Tuple and Set in Python?
    # 有序列表
        # List: 可以新增、刪除、修改、查詢 List 中的元素，list 中的元素可重複。查詢效能是 O(n)
        # Tuple: 是唯獨的且還可用於建立多型別的資料集合。查詢效能是 O(n)
    # 無序列表
        # Dictionary: 可以新增、刪除、修改、查詢 Dictionary 中的元素，Dictionary 中的 Key 不可重複，Value 可重複。查詢效能是 O(1)
        # Set: 可以新增、刪除、修改、查詢 Set 中的元素，Set 中的元素不可重複。查詢效能是 O(1)


#test question1 and question2
if __name__ == '__main__':
    #question1 #find_max
    print('question1 #find_max')
    find_max = my_package.question1.find_max
    numbers = [1, 2, 4, 5]
    max = find_max(numbers)
    print(max)
    numbers = [5, 2, 7, 1, 6]
    max = find_max(numbers)
    print(max)
    #find_max <= empty list
    try :
        numbers = []
        max = find_max(numbers)
        print(max)
    except Exception as e:
        print(e)
    #find_max <= other data type
    try :
        numbers = [1, 2, 'a', 5]
        max = find_max(numbers)
        print(max)
    except Exception as e:
        print(e)
    #question1 #find position
    print('question1 #find position')
    find_position = my_package.question1.find_position
    numbers = [5, 2, 7, 1, 6]
    position = find_position(numbers, 5)
    print(position)
    numbers = [5, 2, 7, 1, 6]
    position = find_position(numbers, 7)
    print(position)
    numbers = [5, 2, 7, 7, 7, 1, 6]
    position = find_position(numbers, 7)
    print(position)
    numbers = [5, 2, 7, 1, 6]
    position = find_position(numbers, 8)
    print(position)

    #question2 #count
    print('question2 #count')
    count = my_package.question2.count
    characters = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
    result = count(characters)
    print(result)
    #question2 #group_by_key
    print('question2 #group_by_key')
    group_by_key = my_package.question2.group_by_key
    objects = [
        {'key': 'a', 'value': 3},
        {'key': 'b', 'value': 1},
        {'key': 'c', 'value': 2},
        {'key': 'a', 'value': 3},
        {'key': 'c', 'value': 5}
    ]
    result = group_by_key(objects)
    print(result)