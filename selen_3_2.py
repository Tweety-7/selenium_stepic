    # ваша реализация, напишите assert и сообщение об ошибке
def test_input_text(expected_result, actual_result):
    # assert  expected_result != actual_result, ""
    assert expected_result == actual_result, "expected {}, got {}".format(expected_result, actual_result)

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

     # ваша реализация, напишите assert и сообщение об ошибке
def test_substring(full_string, substring):
    assert substring in full_string, "expected {} to be substring of {}".format(substring, full_string)

