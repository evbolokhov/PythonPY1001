if __name__ == "__main__":
    # Write your solution here
        list_ = [7, 4, 2, 10, 21, 36, 43, 22, 13, 0]
        first_value = list_[0]
        max_value_index = 0
        max_value = list_[max_value_index]
        for index, current_value in enumerate(list_):
            if current_value >= max_value:
                max_value = current_value
                max_value_index = index
        del list_[max_value_index]
        list_.insert(max_value_index, first_value)
        del list_[0]
        list_.insert(0, max_value)
        print(list_)
